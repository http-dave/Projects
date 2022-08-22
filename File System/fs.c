/*
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wsizeof-array-argument"
#pragma ide diagnostic ignored "bugprone-sizeof-expression"
*/
/*
 * file:        homework.c
 * description: skeleton file for CSX492 file system
 *
 * Credit:
 * 	Peter Desnoyers, November 2016
 * 	Philip Gust, March 2019
 */

#define FUSE_USE_VERSION 27

#include <stdlib.h>
#include <stddef.h>
#include <unistd.h>
//#include <dirent.h> //added to open directory
#include <fuse.h>
#include <fcntl.h>
#include <string.h>
#include <stdio.h>
#include <errno.h>
#include <stdbool.h>

#include "fsx492.h"
#include "blkdev.h"

/* 
 * disk access - the global variable 'disk' points to a blkdev
 * structure which has been initialized to access the image file.
 *
 * NOTE - blkdev access is in terms of 1024-byte blocks
 */
extern struct blkdev *disk; //see main.c

//DIR *directorystream;

/*
 * CS492: feel free to add any data structures, external variables, functions you wanp t to add here
*/
struct fs_super *fsx;  //our global superblock
void *inode_map;	   //our inode map
void *block_map;	   //our block_map
void *inode_table;	   //our table for storing inodes
struct fs_inode *root; //root direcotry
unsigned int err = 0;  // our own errno

int data_block_offset;
/* 
 ********************* Fuse functions
*/

/*
 * init - this is called once by the FUSE frameworX at startup.
 *
 * This is a good place to read in the super-block and set up any
 * global variables you need. You don't need to worry about the
 * argument or the return value.
 *
 * @param conn: fuse connection information - unused
 *
 * @return: unused - returns NULL
*/
void *fs_init(struct fuse_conn_info *conn)
{
	//CS492: your code here
	//allocate the super block
	fsx = (struct fs_super *)malloc(FS_BLOCK_SIZE);

	//read first block from blkdev into fsx since its the superblock
	disk->ops->read(disk, 0, 1, fsx);

	inode_map = (fd_set *)malloc(fsx->inode_map_sz * FS_BLOCK_SIZE);
	//READ IN inode_map from the disk
	disk->ops->read(disk, 1, fsx->inode_map_sz, inode_map);

	//Initialize the block map and read in the block bit map from image
	block_map = (fd_set *)malloc(fsx->block_map_sz * FS_BLOCK_SIZE);
	disk->ops->read(disk, 1 + fsx->inode_map_sz, fsx->block_map_sz, block_map);

	//Initialize the inode table
	inode_table = malloc(fsx->inode_region_sz * FS_BLOCK_SIZE);
	disk->ops->read(disk, 1 + fsx->inode_map_sz + fsx->block_map_sz, fsx->inode_region_sz, inode_table);

	root = inode_table; //start at inode 1
	//since root is a fs_inode* it moves up by 64 bytes with each increment
	//so if root = current, current + 64 = root + 1
	root = root + 1;

	data_block_offset = fsx->block_map_sz + fsx->inode_map_sz + 1 + fsx->inode_region_sz;
	return NULL;
}

struct fs_inode *getInodeFromPath(const char *path, struct fs_inode *result)
{
	//points us to the element / inode in the path
	char *token; //path
	char *copy1;
	char *copy2;
	int block_i = 0;
	int direct_i = 0;
	struct fs_inode *current = root;
	uint32_t *sub = NULL;
	struct fs_dirent temp;
	void *block;
	void *block_iter;
	uint32_t i = 1;
	int num_components = 0; // number of components in path name
	int num = 1;
	int found = 0; //if component was found

	//clear errno
	err = 0;
	if (strcmp(path, "/") == 0 || strcmp(path, "") == 0)
	{
		//if root direcory was input as path
		result = root;
		return result;
	}

	copy1 = strdup(path);
	copy2 = strdup(path);
	block = malloc(FS_BLOCK_SIZE);
	block_iter = block;

	//to get number of path elements
	//ineffecient but should work
	token = strtok(copy1, "/");
	while (token != NULL)
	{
		num_components++;
		token = strtok(NULL, "/");
	}

	token = strtok(copy2, "/");

	while (token != NULL)
	{
		//iterate through tokens
		sub = current->direct;
		direct_i = 0;
		while (direct_i < 1)
		{
			//Only look at first element in direct array
			disk->ops->read(disk, *sub, 1, block);

			block_i = 0;
			while (block_i < DIRENTS_PER_BLK)
			{
				// loop through dirents in the block
				temp = *(struct fs_dirent *)block_iter;
				if (strcmp(token, temp.name) == 0)
				{
					//the path is found move up current to that inode
					if ((temp.isDir == 0 || temp.valid == 0) && num != num_components)
					{
						//if the path was found but element is not a dir or is not valid rerurn null
						err = ENOTDIR;
						result = NULL;
						free(block);
						free(copy1);
						free(copy2);
						return NULL;
					}
					//move our inode pointer to the next inode
					current = current + ((temp.inode - i));
					//set i to our new inode spot
					i = temp.inode;
					//we found component of path in block
					found = 1;
					if (num == num_components)
					{
						result = current;
						free(copy1);
						free(copy2);
						free(block);
						return result;
					}
					break;
				}
				//move block iterator
				block_iter = block_iter + sizeof(struct fs_dirent);
				block_i++;
				found = 0;
			}
			direct_i++;
			block_iter = block;
		}
		if (found == 0)
		{
			//if component of a path was not found return
			err = ENOENT;
			result = NULL;
			free(block);
			free(copy1);
			free(copy2);
			return NULL;
		}
		num++;
		token = strtok(NULL, "/");
	}
	if (found == 0)
	{
		//if component of a path was not found return null
		err = ENOENT;
		result = NULL;
		free(block);
		free(copy1);
		free(copy2);
		return NULL;
	}
	result = current;
	free(block);
	free(copy1);
	free(copy2);
	return result;
}

struct fs_dirent getDirentFromPath(const char *path, struct fs_dirent result)
{
	//points us to the element / inode in the path
	char *token; //path
	char *copy1;
	char *copy2;
	int block_i = 0;
	int direct_i = 0;
	struct fs_inode *current = root;
	uint32_t *sub = NULL;
	void *block;
	void *block_iter;
	uint32_t i = 1;
	int num_components = 0; // number of components in path name
	int num = 1;
	int found = 0; //if component was found

	//clear errno
	err = 0;
	if (strcmp(path, "/") == 0 || strcmp(path, "") == 0)
	{
		//if root direcory was input as path
		result.inode = 1; //still don't know where to find dirent of root
		return result;
	}

	copy1 = strdup(path);
	copy2 = strdup(path);
	block = malloc(FS_BLOCK_SIZE);
	block_iter = block;

	//to get number of path elements
	//ineffecient but should work
	token = strtok(copy1, "/");
	while (token != NULL)
	{
		num_components++;
		token = strtok(NULL, "/");
	}

	token = strtok(copy2, "/");

	while (token != NULL)
	{
		//iterate through tokens
		sub = current->direct;
		direct_i = 0;
		while (direct_i < 1)
		{
			//Only look at first element in direct array
			disk->ops->read(disk, *sub, 1, block);

			block_i = 0;
			while (block_i < DIRENTS_PER_BLK)
			{
				// loop through dirents in the block
				result = *(struct fs_dirent *)block_iter;
				if (strcmp(token, result.name) == 0)
				{
					//the path is found move up current to that inode
					if ((result.isDir == 0 || result.valid == 0) && num != num_components)
					{
						//if the path was found but element is not a dir or is not valid rerurn null
						err = ENOTDIR;
						result.inode = 0;
						free(block);
						free(copy1);
						free(copy2);
						return result;
					}
					//move our inode pointer to the next inode
					current = current + ((result.inode - i));
					//set i to our new inode spot
					i = result.inode;
					//we found component of path in block
					found = 1;
					if (num == num_components)
					{
						free(copy1);
						free(copy2);
						free(block);
						return result;
					}
					break;
				}
				block_iter = block_iter + sizeof(struct fs_dirent);
				block_i++;
				found = 0;
			}
			direct_i++;
			block_iter = block;
		}
		if (found == 0)
		{
			//if component of a path was not found return
			err = ENOENT;
			result.inode = 0;
			free(block);
			free(copy1);
			free(copy2);
			return result;
		}
		num++;
		token = strtok(NULL, "/");
	}
	if (found == 0)
	{
		//if component of a path was not found return null
		err = ENOENT;
		result.inode = 0;
		free(block);
		free(copy1);
		free(copy2);
		return result;
		;
	}
	free(block);
	free(copy1);
	free(copy2);
	return result;
}

/*
 * getattr - get file or directory attributes. For a description of
 * the fields in 'struct stat', see 'man lstat'.
 *
 * Note - you can handle some fields as follows:
 * st_nlink - always set to 1
 * st_atime, st_ctime - set to same value as st_mtime
 *
 * @param path: the file path
 * @param sb: pointer to stat struct
 *
 * @return: 0 if successful, or -error number
 * 	-ENOENT  - a component of the path is not present
 *	-ENOTDIR - an intermediate component of path not a directory
*/
static int fs_getattr(const char *path, struct stat *sb)
{
	//https://linux.die.net/man/2/lstat

	//CS492: your code here
	//this is for the cd command
	//int retval;
	struct fs_inode *current;
	errno = 0;

	current = getInodeFromPath(path, NULL);
	//build stat struct in sb from path
	if (current == NULL)
	{
		//if unsuccessful
		if (err == ENOENT)
		{
			//if path was empty or not found
			fprintf(stderr, "Path could not be found. (fs_getattr)\n");
			return -ENOENT;
		}
		if (err == ENOTDIR)
		{
			//if path was empty or not found
			fprintf(stderr, "Component of path was not a directory. (fs_getattr)\n");
			return -ENOTDIR;
		}
	}
	sb->st_uid = current->uid;	 //user id
	sb->st_gid = current->gid;	 //grouping to owner that created the file
	sb->st_mode = current->mode; //
	//set values given to us
	sb->st_nlink = 2;
	//setting time of last access = time of last modification
	sb->st_mtime = sb->st_mtime;
	//last status change = time of last modification
	sb->st_ctime = sb->st_mtime;
	//return success
	return 0;
}

/*
 * open - open file directory
 *
 * You can save information about the open directory in fi -> fh. If you allocate memory, free it in fs_releasedir.
 *
 * @param path: the file path
 * @param fi: fuse file system information
 *
 * @return: 0 if successful, or -error number
 *	-ENOENT  - a component of the path is not present
 *	-ENOTDIR - an intermediate component of path not a directory
*/
static int fs_opendir(const char *path, struct fuse_file_info *fi)
{
	//CS492: your code here
	//directory stream
	struct fs_dirent temp;
	temp = getDirentFromPath(path, temp);
	if (temp.inode == 0)
	{
		if (err == ENOTDIR)
		{
			return -ENOTDIR;
		}
		if (err == ENOENT)
		{
			return -ENOENT;
		}
	}
	fi->fh = temp.inode;
	return 0;
}

/*
    readdir - get directory contents

    For each entry in the directory, invoke the 'filler' function, which is passed as a function pointer, as follows:
    filler(buf, <name>, <statbuf>, 0) where <statbuf> is a struct stat, just like in getattr.

    @param path: the directory path
    @param ptr: filler buf pointer
    @param filler filler function to call for each entry
    @param offset: the file offset -- unused
    @param fi: the fuse file information -- you do not have to use it

    @return: 0 if successful, or -error number
    	-ENOENT  - a component of the path is not present
    	-ENOTDIR - an intermediate component of path not a directory
*/
//fs -> fh should be current dirrectory inode and get the specific inode as well
//have to utilize fi->fh from opendir
static int fs_readdir(const char *path, void *ptr, fuse_fill_dir_t filler,
					  off_t offset, struct fuse_file_info *fi)
{

	//CS492: your code here
	struct fs_inode *current;
	char *block = malloc(FS_BLOCK_SIZE);
	char *block_iter = block;
	struct fs_dirent temp;
	uint32_t *sub;
	struct stat sb;
	int block_i = 0;
	int direct_i = 0;

	current = getInodeFromPath(path, NULL);
	if (current == NULL)
	{
		if (err == ENOENT)
		{
			free(block);
			return -ENOENT;
		}
		if (err == ENOTDIR)
		{
			free(block);
			return -ENOTDIR;
		}
	}
	sub = current->direct;
	direct_i = 0;
	while (direct_i < 1)
	{
		//Only look at first element in direct array
		disk->ops->read(disk, *sub, 1, block);

		block_i = 0;
		while (block_i < DIRENTS_PER_BLK)
		{
			// loop through dirents in the block
			temp = *(struct fs_dirent *)block_iter;
			if (temp.inode != 0)
			{
				//if dirents are empty don't call filler on them
				filler(ptr, temp.name, &sb, 0);
			}
			block_iter = block_iter + sizeof(struct fs_dirent);
			block_i++;
		}
		direct_i++;
		block_iter = block;
	}

	free(block);

	return 0;
}

/*
 * Release resources when directory is closed.
 * If you allocate memory in fs_opendir, free it here.
 *
 * @param path: the directory path
 * @param fi: fuse file system information -- you do not have to use it 
 *
 * @return: 0 if successful, or -error number
 *	-ENOENT  - a component of the path is not present
 *	-ENOTDIR - an intermediate component of path not a directory
*/
static int fs_releasedir(const char *path, struct fuse_file_info *fi)
{
	//CS492: your code here
	//set the new file handle to zero

	fi->fh = 0;
	return 0;
}

/*
 * mknod - create a new file with permissions (mode & 01777). Behavior undefined when mode bits other than the low 9 bits are used.
 * 	
 * @param path: the file path
 * @param mode: indicating block or character-special file
 * @param dev: the character or block I/O device specification - you do not have to use it
 * 			 
 * @return: 0 if successful, or -error number
 * 	-ENOTDIR  - component of path not a directory
 * 	-EEXIST   - file already exists
 * 	-ENOSPC   - free inode not available
 * 	-ENOSPC   - results in >32 entries in directory
*/
static int fs_mknod(const char *path, mode_t mode, dev_t dev)
{
	//CS492: your code here
	struct fs_dirent file_ent;
	struct fs_dirent temp;
	struct fs_inode file_inode;
	struct fs_inode *current;
	void *block = malloc(FS_BLOCK_SIZE);
	char *block_iter;
	int block_i = 0;
	char *token;
	int num_tokens = 0;
	char *copy = strdup(path);
	char *copy2 = strdup(path);
	int num = 1;
	char *one_less = (char *)malloc(strlen(path));
	int i = 0;
	struct fs_inode *free_inode = root;
	int inode_i = 1;
	time_t curtime;

	file_ent.valid = 1;
	file_inode.uid = getuid();
	file_inode.gid = getgid();
	file_inode.mode = mode;
	file_inode.ctime = time(&curtime);
	file_inode.mtime = time(&curtime);
	file_inode.size = 0;

	memset(one_less, '\0', strlen(path));
	token = strtok(copy, "/");
	while (token != NULL)
	{

		num_tokens++;
		token = strtok(NULL, "/");
	}
	free(copy);
	memset(file_ent.name, '\0', FS_FILENAME_SIZE);
	token = strtok(copy2, "/");
	while (token != NULL)
	{
		if (num == num_tokens)
		{
			for (i = 0; i < strlen(token); i++)
			{
				file_ent.name[i] = token[i];
			}
			file_ent.name[strlen(token)] = '\0';
			break;
		}
		strcat(one_less, "/");
		strcat(one_less, token);
		num++;
		token = strtok(NULL, "/");
	}

	current = getInodeFromPath(one_less, NULL);
	if (current == NULL)
	{
		if (err == ENOENT)
		{
			free(block);
			free(copy2);
			free(one_less);
			return -ENOENT;
		}
		if (err == ENOTDIR)
		{
			free(block);
			free(copy2);
			free(one_less);
			return -ENOTDIR;
		}
	}
	file_inode.direct[0] = current->direct[0];

	while (free_inode->mode != 0 && (inode_i < fsx->inode_region_sz * INODES_PER_BLK))
	{
		//find a free inode
		free_inode++;
		inode_i++;
	}
	if (inode_i >= fsx->inode_region_sz * INODES_PER_BLK)
	{
		// there are no available inodes
		free(block);
		free(copy2);
		free(one_less);
		return -ENOSPC;
	}

	//set that inode number to new directory entry
	file_ent.inode = inode_i;
	disk->ops->read(disk, current->direct[0], 1, block);

	while (block_i < DIRENTS_PER_BLK)
	{
		// loop through dirents in the block
		temp = *(struct fs_dirent *)block_iter;
		if (temp.inode == 0)
		{
			//store the file entry in empty block spot
			*(struct fs_dirent *)block_iter = file_ent;
			//store the inode in available inode spot
			*free_inode = file_inode;
			disk->ops->write(disk, current->direct[0], 1, block);
			disk->ops->write(disk, 1 + fsx->inode_map_sz + fsx->block_map_sz, fsx->inode_region_sz, inode_table);
			free(block);
			free(copy2);
			free(one_less);
			return 0;
		}
		block_iter = block_iter + sizeof(struct fs_dirent);
		block_i++;
	}
	//if we get here directory is full

	free(block);
	free(copy2);
	free(one_less);

	return -ENOSPC;
}

/*
 * 	mkdir - create a directory with the given mode. Behavior undefined when mode bits other than the low 9 bits are used.
 *
 * 	@param path: path to directory
 * 	@param mode: the mode for the new directory
 *
 * 	@return: 0 if successful, or -error number
 * 		-ENOTDIR  - component of path not a directory
 * 		-EEXIST   - file already exists
 * 		-ENOSPC   - free inode not available
 * 		-ENOSPC   - results in >32 entries in directory
*/
static int fs_mkdir(const char *path, mode_t mode)
{
	//CS492: your code here
	struct fs_dirent file_ent;
	struct fs_dirent temp;
	struct fs_inode file_inode;
	struct fs_inode *current;
	void *block = malloc(FS_BLOCK_SIZE);
	char *block_iter;
	int block_i = 0;
	char *token;
	int num_tokens = 0;
	char *copy = strdup(path);
	char *copy2 = strdup(path);
	int num = 1;
	char *one_less = (char *)malloc(strlen(path));
	int i = 0;
	struct fs_inode *free_inode = root;
	int inode_i = 1;
	time_t curtime;

	file_ent.valid = 1;
	file_ent.isDir = 1;
	file_inode.uid = getuid();
	file_inode.gid = getgid();
	file_inode.mode = mode;
	file_inode.ctime = time(&curtime);
	file_inode.mtime = time(&curtime);
	file_inode.size = 0;

	memset(one_less, '\0', strlen(path));
	token = strtok(copy, "/");
	while (token != NULL)
	{

		num_tokens++;
		token = strtok(NULL, "/");
	}
	free(copy);
	memset(file_ent.name, '\0', FS_FILENAME_SIZE);
	token = strtok(copy2, "/");
	while (token != NULL)
	{
		if (num == num_tokens)
		{
			for (i = 0; i < strlen(token); i++)
			{
				file_ent.name[i] = token[i];
			}
			file_ent.name[strlen(token)] = '\0';
			break;
		}
		strcat(one_less, "/");
		strcat(one_less, token);
		num++;
		token = strtok(NULL, "/");
	}

	current = getInodeFromPath(one_less, NULL);
	if (current == NULL)
	{
		if (err == ENOENT)
		{
			free(block);
			free(copy2);
			free(one_less);
			return -ENOENT;
		}
		if (err == ENOTDIR)
		{
			free(block);
			free(copy2);
			free(one_less);
			return -ENOTDIR;
		}
	}
	file_inode.direct[0] = current->direct[0];

	while (free_inode->mode != 0 && (inode_i < fsx->inode_region_sz * INODES_PER_BLK))
	{
		//find a free inode
		free_inode++;
		inode_i++;
	}
	if (inode_i >= fsx->inode_region_sz * INODES_PER_BLK)
	{
		// there are no available inodes
		free(block);
		free(copy2);
		free(one_less);
		return -ENOSPC;
	}

	//set that inode number to new directory entry
	file_ent.inode = inode_i;
	disk->ops->read(disk, current->direct[0], 1, block);

	while (block_i < DIRENTS_PER_BLK)
	{
		// loop through dirents in the block
		temp = *(struct fs_dirent *)block_iter;
		if (temp.inode == 0)
		{
			//store the file entry in empty block spot
			*(struct fs_dirent *)block_iter = file_ent;
			//store the inode in available inode spot
			*free_inode = file_inode;
			disk->ops->write(disk, current->direct[0], 1, block);
			disk->ops->write(disk, 1 + fsx->inode_map_sz + fsx->block_map_sz, fsx->inode_region_sz, inode_table);
			free(block);
			free(copy2);
			free(one_less);
			return 0;
		}
		block_iter = block_iter + sizeof(struct fs_dirent);
		block_i++;
	}
	//if we get here directory is full

	free(block);
	free(copy2);
	free(one_less);

	return -ENOSPC;
}

/*
 * unlink - delete a file
 *
 * @param path: path to file
 *
 * @return 0 if successful, or error value
 *	-ENOENT   - file does not exist
 * 	-ENOTDIR  - component of path not a directory
 * 	-EISDIR   - cannot unlink a directory
*/
static int fs_unlink(const char *path)
{
	/*
	struct fs_inode *c_inode;
	c_inode = malloc(sizeof(struct fs_inode));
	c_inode = getInodeFromPath(path, NULL);
	//CS492: your code here
	int retval = 0;
	retval = unlink(path);
	if (retval < 0)
	{
		if (errno == ENOENT)
		{
			//if file does not exist
			printf(stderr, "File does not exist in directory. (fs_unlink)\n");
			return -ENOENT;
		}
		if (errno == ENOTDIR)
		{
			//if component of path was not found
			fprintf(stderr, "Component of path could not be found. (fs_unlink)\n", path);
			return -ENOTDIR;
		}
		if (errno == EISDIR)
		{
			//if path is a directory
			fprintf(stderr, "Cannot delete a directory. (fs_unlink).\n", path);
			return -EISDIR;
		}

	}
	*/
	return -1;
}

/*
 * rmdir - remove a directory
 *
 * @param path: the path of the directory
 *
 * @return: 0 if successful, or -error number
 * 		-ENOENT   - file does not exist
 *  	-ENOTDIR  - component of path not a directory
 *  	-ENOTDIR  - path not a directory
 *  	-ENOTEMPTY - directory not empty
*/
static int fs_rmdir(const char *path)
{
	/*
	//CS492: your code here
	int retval = 0;
	retval = rmdir(path);
	if (retval < 0)
	{
		if (err == ENOENT)
		{
			//if file does not exist
			fprintf(stderr, "File does not exist in directory. (fs_rmdir)\n");
			return -ENOENT;
		}
		if (err == ENOTDIR)
		{
			//if component of path was not found
			fprintf(stderr, "Component of path could not be found. (fs_rmdir)\n", path);
			return -ENOTDIR;
		}
		if (err == ENOTEMPTY)
		{
			//if path is a directory
			fprintf(stderr, "Directory is not empty. (fs_rmdir)\n", path);
			return -ENOTEMPTY;
		}
	}
*/
	return -1;
}

/*
 * rename - rename a file or directory. You can assume the destination and the source share the same path-prefix
 *
 * Note that this is a simplified version of the UNIX rename
 * functionality - see 'man 2 rename' for full semantics. In
 * particular, the full version can move across directories, replace a destination file, and replace an empty directory with a full one.
 *  
 *  	@param src_path: the source path
 *  	@param dst_path: the destination path
 *
 *  	@return: 0 if successful, or -error number
 *  		-ENOENT   - source file or directory does not exist
 *  		-ENOTDIR  - component of source or target path not a directory
 *  		-EEXIST   - destination already exists
 *  		-EINVAL   - source and destination not in the same directory
*/
static int fs_rename(const char *src_path, const char *dst_path)
{
	/*
	//CS492: your code here
	int retval = 0;
	retval = rename(src_path, dst_path);
	if (retval < 0)
	{
		if (errno == ENOENT)
		{
			//if file does not exist
			fprintf(stderr, "File does not exist in directory. (fs_rename)\n");
			return -ENOENT;
		}
		if (errno == ENOTDIR)
		{
			//if component of path was not found
			fprintf(stderr, "Component of path could not be found. (fs_rename)\n", dst_path);
			return -ENOTDIR;
		}
		if (errno == EEXIST)
		{
			//if path is a directory
			fprintf(stderr, "Destination already exisit.\n");
			return -EEXIST;
		}
		if (errno == EINVAL)
		{
			fprintf(stderr, "Source and destination are not in the same directory. (fs_rename)\n");
			return -EINVAL;
		}
	}
*/
	return -1;
}

/*
 * chmod - change file permissions
 *
 * @param path: the file or directory path
 * @param mode: the mode_t mode value -- see man 'chmod'
 * for description
 *
 *  @return: 0 if successful, or -error number
 *  	-ENOENT   - file does not exist
 *  	-ENOTDIR  - component of path not a directory
*/
static int fs_chmod(const char *path, mode_t mode)
{
	//CS492: your code here
	struct fs_inode *current;
	//get inode of path
	current = getInodeFromPath(path, NULL);
	if (current == NULL)
	{
		if (err == ENOENT)
		{
			return -ENOENT;
		}
		if (err == ENOTDIR)
		{
			return -ENOTDIR;
		}
	}
	//set the mode to new mode
	current->mode = mode;
	//write new inode table back into block
	disk->ops->write(disk, 1 + fsx->inode_map_sz + fsx->block_map_sz, fsx->inode_region_sz, inode_table);

	return 0;
}

/*
 * Open a filesystem file or directory path.
 *
 * @param path: the path
 * @param fuse: file info data
 *
 * @return: 0 if successful, or -error number
 *	-ENOENT   - file does not exist
 *	-ENOTDIR  - component of path not a directory
*/
static int fs_open(const char *path, struct fuse_file_info *fi)
{
	//CS492: your code here
	/*
	int retval = 0;
	open_fs = fopen(path, "r+");
	if (open_fs == NULL)
	{
		if (errno == ENOENT)
		{
			//if file does not exist
			fprintf(stderr, "File does not exist in directory. (fs_open)\n");
			return -ENOENT;
		}
		if (errno == ENOTDIR)
		{
			//if component of path was not found
			fprintf(stderr, "Component of path could not be found. (fs_open)\n");
			return -ENOTDIR;
		}
	}
*/
	return -1;
}

/*
 * read - read data from an open file.
 *
 * 	@param path: the path to the file
 * 	@param buf: the buffer to keep the data
 * 	@param len: the number of bytes to read
 * 	@param offset: the location to start reading at
 * 	@param fi: fuse file info
 *
 * 	@return: return exactly the number of bytes requested, except:
 * 	- if offset >= file len, return 0
 * 	- if offset+len > file len, return bytes from offset to EOF
 * 	- on error, return <0
 * 		-ENOENT  - file does not exist
 * 		-ENOTDIR - component of path not a directory
 * 		-EIO     - error reading block
*/
static int fs_read(const char *path, char *buf, size_t len, off_t offset,
				   struct fuse_file_info *fi)
{
	/*
	//CS492: your code here
	fi->fh;
	struct fs_inode *ok;
	errno = 0;
	getInodeFromPath(path, ok);
*/
	return -1;
}

/*
 * write - write data to a file
 *
 * @param path: the file path
 * @param buf: the buffer to write
 * @param len: the number of bytes to write
 * @param offset: the offset to starting writing at
 * @param fi: the Fuse file info for writing
 *
 * @return: It should return exactly the number of bytes requested, except on error:
 * 	-ENOENT  - file does not exist
 *	-ENOTDIR - component of path not a directory
 *	-EINVAL  - if 'offset' is greater than current file length. (POSIX semantics support the creation of files with "holes" in them, but we don't)
*/
static int fs_write(const char *path, const char *buf, size_t len,
					off_t offset, struct fuse_file_info *fi)
{
	//CS492: your code here

	return -1;
}

/*
 * Release resources created by pending open call.
 *
 * @param path: path to the file
 * @param fi: the fuse file info
 *
 * @return: 0 if successful, or -error number
 *	-ENOENT   - file does not exist
 *	-ENOTDIR  - component of path not a directory
*/
static int fs_release(const char *path, struct fuse_file_info *fi)
{
	//CS492: your code here
	return -1;
}

/*
 * statfs - get file system statistics. See 'man 2 statfs' for description of 'struct statvfs'.
 *
 * @param path: the path to the file
 * @param st: pointer to the destination statvfs struct
 *
 * @return: 0 if successful, or -error number
 * 	-ENOENT  - a component of the path is not present
 *	-ENOTDIR - an intermediate component of path not a directory
*/
static int fs_statfs(const char *path, struct statvfs *st)
{
	//CS492: your code here
	struct fs_inode *current;
	struct fs_inode *free_inode = root;
	int i = 1;
	int free_nodes = 0;
	current = getInodeFromPath(path, NULL);
	if (current == NULL)
	{
		//check current result
		if (err == ENOENT)
		{
			return -ENOENT;
		}
		if (err == ENOTDIR)
		{
			return -ENOTDIR;
		}
	}
	while (i < fsx->inode_region_sz * INODES_PER_BLK)
	{
		//find free inodes
		if (free_inode->mode == 0)
		{
			free_nodes++;
		}
		//increment pointer
		free_inode++;
		i++;
	}
	//set values in struct
	st->f_ffree = (fsblkcnt_t)free_nodes;
	st->f_fsid = (unsigned long)FS_MAGIC;
	st->f_bsize = (unsigned long)FS_BLOCK_SIZE;
	st->f_blocks = (fsblkcnt_t)fsx->num_blocks;
	st->f_files = (fsfilcnt_t)fsx->inode_region_sz * INODES_PER_BLK;
	st->f_namemax = (unsigned long)FS_FILENAME_SIZE;

	//return success
	return 0;
}

/**
 * Operations vector. Please don't rename it, as the
 * skeleton code in misc.c assumes it is named 'fs_ops'.
 */
struct fuse_operations fs_ops = {
	.init = fs_init,
	.getattr = fs_getattr,
	.opendir = fs_opendir,
	.readdir = fs_readdir,
	.releasedir = fs_releasedir,
	.mknod = fs_mknod,
	.mkdir = fs_mkdir,
	.unlink = fs_unlink,
	.rmdir = fs_rmdir,
	.rename = fs_rename,
	.chmod = fs_chmod,
	.open = fs_open,
	.read = fs_read,
	.write = fs_write,
	.release = fs_release,
	.statfs = fs_statfs,
};

/*#pragma clang diagnostic pop*/
