/*
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
Author: Dave Taveras
Date: May 3rd, 2020
Assignment: HW3 cs392_shell: cs392_exec.c file
Course: CS 392 Systems Programming
*/


/*This file will contain the functions to run each command from the user*/
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/wait.h>
#include"cs392_exec.h"

char* read_input(char* buf){
    //Function to read input from the user
    int index = 0;
    int ch;
    
    while(1){
        //Read a character
        ch = getchar();
        
        if(ch == EOF || ch == '\n'){
            //if EOF is read, replace it with a null byte and return the input
            buf[index] = '\0';
            return buf;
        }else{
            //add the character to buffer
            buf[index] = ch;
        }
        //incrememnt index
        index++;
    }
}


void execute_commands(char* line){
    //Function to execute commands
    char** args = malloc(1024*sizeof(char*)); //left side of pipe array
    char** piping = malloc(1024*sizeof(char*)); //right side of pipe array
    char* token;
    int index = 0;
    int is_pipe = 0; //variable to determine if there is a pipe
    int word_count = 1;
    
    if(line[0] == 'e' && line[1] == 'x' && line[2] == 'i' && line[3] == 't'){
        //if "exit" is entered then terminate the shell
        free(args);
        free(piping);
        exit(1);
    }
    
    while(line[index] != '\0'){
        //read the characters in the input array
        
        if(line[index] == '|'){
            //if there is a pipe change is_pipe to 1
            is_pipe = 1;
            break;
        }
        if (line[index] == ' '){
            //increment a word count for all arguments found
            word_count++;
        }
        //increment index
        index++;
    }
    //initialize the args array with allocated memory
    for(int i = 0; i<word_count; i++){
        args[i] = malloc(256*sizeof(char));
    }
    
    
    index = 0; //reset index
    if(is_pipe == 1){ // if there is a pipe
        //initialize the piping array with allocated memory
        for(int i = 0; i<word_count; i++){
              piping[i] = malloc(256*sizeof(char));
          }
        //input is guaranteed to have 2 arguments (left of pipe and right of pipe
        char* l_r_args[2];
        
        
        //separate both sides of pipe
        token = strtok(line, "|");
        while(token!=NULL){
            l_r_args[index] = token;
            index++;
            token = strtok(NULL, "|");
        }
        
        
        //remove spaces from left side to get arguments
        index = 0;
        char* argl = strtok(l_r_args[0], " ");
        while(argl!=NULL){
            strcpy(args[index], argl);
            index++;
            argl = strtok(NULL, " ");
        }
        free(args[index]);
        args[index] = NULL;
        
       
        
        //remove spaces from right side to get arguments
        char* argr = strtok(l_r_args[1], " \"");
        index = 0;
        while(argr!=NULL){
            strcpy(piping[index], argr);
            index++;
            argr = strtok(NULL, " \"");
        }
        free(piping[index]);;
        piping[index] = NULL;
        
        
        
        
        //time for the execution of the arguments
        index = 0;
        int pid[2]; //pid for both children
        int fd[2]; //pipe array
        pipe(fd); //initialize the pipe
        
        
        for(int i = 0; i < 2; i++){
           
            pid[i] = fork(); //fork the program 2 times
            if(pid[i] == 0){
                //This is the first child
                if (i == 0){
                    //executes left side of pipe
                    dup2(fd[1], STDOUT_FILENO); //attach to writing end
                    close(fd[0]); //close the reading end
                    execvp(args[0], args); //run the command
                    perror(args[0]); //if it doesn't work
                    exit(EXIT_FAILURE);
                }
                //This is the right child
                if(i == 1){
                    //Executes right side of pipe
                    dup2(fd[0], STDIN_FILENO);  //attach to reading end
                    close(fd[1]);  //close the writing end
                    execvp(piping[0], piping);  //run the command
                    perror(piping[0]);  //if it doesn't work
                    exit(EXIT_FAILURE);
                }
            }
            if(pid[i] < 0){
                //If there is an error forking
                perror("Could not fork");
                //Free the memory that was allocated
                for(int i = 0; i <word_count; i++){
                    free(piping[i]);
                }
                for(int i = 0; i<word_count; i++){
                    free(args[i]);
                }
                free(args);
                free(piping);
                exit(1);
            }
            if(i == 0){
                //close the writing end in the parent of the first child
                close(fd[1]);
            }
            if(i == 1){
                //close the reading end in the parent of the second child
                close(fd[0]);
                
            }
            //wait for both children to finish running in the parent of both
            wait(NULL);
            wait(NULL);
        }
        //Free the memory that was allocated
        for(int i = 0; i <word_count; i++){
            free(piping[i]);
        }
    }
    else if(is_pipe == 0){ //If there is no pipe
        
        //separate the spaces from the input to get arguments
        token = strtok(line, " \"");
        while(token!=NULL){
            strcpy(args[index], token);
            index++;
            token = strtok(NULL, " \"");
        }
        args[index] = NULL;
        
        
        
        pid_t pid; //pid for fork
        
        pid = fork();
        if(pid == 0){
            if(execvp(args[0], args) == -1){
                //if the command is not valid or fails
                perror(args[0]);
            }
            exit(EXIT_FAILURE);
        }else if(pid<0){
            //if there is an error forking
            perror("could not fork");
            //Free the memory that was allocated
            for(int i = 0; i<word_count; i++){
                free(args[i]);
            }
            free(args);
            free(piping);
            exit(1);
            
        }else{
            //wait for the child to execute in the parent
            wait(NULL);
        }
    }
    //Free the memory that was allocated
    for(int i = 0; i<word_count; i++){
        free(args[i]);
    }
    free(args);
    free(piping);
}


