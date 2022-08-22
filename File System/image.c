/*
 * file:        image.c
 * description: skeleton code for CS 7600 / CS5600 Homework 3
 *
 * Peter Desnoyers, Northeastern Computer Science, 2011
 * Philip Gust, Northeastern Computer Science, 2019
 */

#define _XOPEN_SOURCE 500

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <errno.h>
#include <string.h>
#include <time.h>

#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>

#include "blkdev.h"

// should be defined in "string.h" but is not on macos
extern char *strdup(const char *);
//Not working within the kernel in this case atm
/** definition of image block device */
struct image_dev
{
	char *path; // path to device file
	int fd;		// file descriptor of open file
	int nblks;	// number of blocks in device
};

/*
 * 	count the number of blocks on the device
 * 	@param dev: the block device
 * 	@return: the number of blocks in the block device
*/
static int image_num_blocks(struct blkdev *dev)
{
	//CS492: your code here
	struct image_dev *imager = dev->private;
	//private coming from the blkdev header which is the block device private state
	return imager->nblks;
}

/*
 *	read blocks from block device starting at give block index
 * 	@param dev: the block device
 * 	@param first_blk: index of the block to start reading from
 * 	@param nblks: number of blocks to read from the device
 * 	@param buf: buffer to store the data
 * 	@return: return status of the operation (success or error reason -- please refer to blkdev.h for error reasons)
*/
static int image_read(struct blkdev *dev, int first_blk, int nblks, void *buf)
{
	//CS492: your code here
	int res;
	struct image_dev *imager = dev->private;

	if (fcntl(imager->fd, F_GETFD) == -1)
	{
		//File descriptor has been closed return E_UNAVAIL
		fprintf(stderr, "File descriptor is unavailable\n");
		return E_UNAVAIL;
	}
	//if 0 returned, expression returns an errror
	assert(first_blk + nblks <= imager->nblks && first_blk >= 0);
	//pread is used to count bytes from fd at the offset's start of the file
	res = pread(imager->fd, buf, nblks * BLOCK_SIZE, first_blk * BLOCK_SIZE);

	if (res < 0)
	{

		fprintf(stderr, "error on read %s:%s\n", imager->path, strerror(errno));
		assert(0);
	}
	//return success
	return 0;
}

/*
 * write bytes to block device starting at give block index
 * @param dev: the block device
 * @param first_blk: index of the block to start writing to
 * @param nblks: number of blocks to write to the device
 * @param buf: buffer where data comes from
 * @return: return status of the operation (success or error reason -- please refer to blkdev.h for error reasons)
*/
static int image_write(struct blkdev *dev, int first_blk, int nblks, void *buf)
{
	//CS492: your code here
	int res;
	struct image_dev *imager;

	if (dev == NULL)
	{
		//check if the device has been closed
		fprintf(stderr, "Device is unavailable\n");
		return E_UNAVAIL;
	}
	imager = dev->private;

	//ensure that first block and nblks are valid
	assert(first_blk != 0);
	assert(first_blk + nblks <= imager->nblks && first_blk >= 0);
	//pwrite writes to count bytes from the buffer
	res = pwrite(imager->fd, buf, nblks * BLOCK_SIZE, first_blk * BLOCK_SIZE);

	if (res != nblks * BLOCK_SIZE)
	{
		//couldn't write correct number of bytes
		fprintf(stderr, "Error for write %s:%s\n", imager->path, strerror(errno));
		assert(0); //Throw a failure and end the program
	}
	//success
	return 0;
}

/*
 * Flush the block device.
 * @param dev: the block device
 * @aparam first_blk: index of the block to start flushing 
 * @param nblks: number of blocks to flush
 * @return: return status of the operation (success or error reason -- please refer to blkdev.h for error reasons)
*/
static int image_flush(struct blkdev *dev, int first_blk, int nblks)
{
	//CS492: your code here
	int res;
	struct image_dev *imager;

	if (dev == NULL)
	{
		//check if the device has been closed
		fprintf(stderr, "Device is unavailable.\n");
		return E_UNAVAIL;
	}
	imager = dev->private;
	//buffer that contains correct amount of zeros to store
	void *buf = NULL;
	buf = malloc(nblks * BLOCK_SIZE);
	memset(buf, 0, nblks * BLOCK_SIZE);
	if (buf == NULL)
	{
		//buf was not properly initialized
		fprintf(stderr, "Buf was not properly initialized in image_flush.\n");
		assert(0);
	}
	//ensure that there is no failure in first_blk
	assert(first_blk != 0);
	assert(first_blk + nblks <= imager->nblks && first_blk >= 0);
	//pwrite those zeros from buf into image fd
	res = pwrite(imager->fd, buf, nblks * BLOCK_SIZE, first_blk * BLOCK_SIZE);
	//free buf
	free(buf);

	if (res != nblks * BLOCK_SIZE)
	{
		//if correct number of zeros could not be written to image
		fprintf(stderr, "Error for write %s: %s\n", imager->path, strerror(errno));
		assert(0); //Throw a failure and end the program
	}
	//success
	return 0;
}

/* 
 * close the device. After this, access to device will return errors
 * @param dev: the block device
*/
static void image_close(struct blkdev *dev)
{
	//CS492: your code here
	struct image_dev *imager;
	if (dev == NULL)
	{
		//check if the device has already been closed
		fprintf(stderr, "Device is unavailable.\n");
		return;
	}
	imager = dev->private;
	//close file descriptor
	close(imager->fd);
	imager->fd = -1; //after closing we want to set the fd to an invalid file descriptor value in order to ensure nothing is open
	//free the imager and set to NULL
	free(imager);
	imager = NULL;
	//free the blkdev and set to NULL
	free(dev);
	dev = NULL;
	return;
}

/** Operations on this block device */
static struct blkdev_ops image_ops = {
	.num_blocks = image_num_blocks,
	.read = image_read,
	.write = image_write,
	.flush = image_flush,
	.close = image_close};

/**
 * Create an image block device reading from a specified image file.
 *
 * @param path the path to the image file
 * @return the block device or NULL if cannot open or read image file
 */
struct blkdev *image_create(char *path)
{
	struct blkdev *dev = malloc(sizeof(*dev));
	struct image_dev *im = malloc(sizeof(*im));

	if (dev == NULL || im == NULL)
		return NULL;

	im->path = strdup(path); /* save a copy for error reporting */

	/* open image device */
	im->fd = open(path, O_RDWR);
	if (im->fd < 0)
	{
		fprintf(stderr, "can't open image %s: %s\n", path, strerror(errno));
		return NULL;
	}

	/* access image device */
	struct stat sb;
	if (fstat(im->fd, &sb) < 0)
	{
		fprintf(stderr, "can't access image %s: %s\n", path, strerror(errno));
		return NULL;
	}

	/* print a warning if file is not a multiple of the block size -
     * this isn't a fatal error, as extra bytes beyond the last full
     * block will be ignored by read and write.
     */
	if (sb.st_size % BLOCK_SIZE != 0)
	{
		fprintf(stderr, "warning: file %s not a multiple of %d bytes\n",
				path, BLOCK_SIZE);
	}
	im->nblks = sb.st_size / BLOCK_SIZE;
	dev->private = im;
	dev->ops = &image_ops;

	return dev;
}

/**
 * Force an image blkdev into failure. After this any
 * further access to that device will return E_UNAVAIL.
 */
void image_fail(struct blkdev *dev)
{
	struct image_dev *im = dev->private;

	if (im->fd != -1)
	{
		close(im->fd);
	}
	im->fd = -1;
}
