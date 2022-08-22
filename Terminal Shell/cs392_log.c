/*
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
Author: Dave Taveras
Date: May 3rd, 2020
Assignment: HW3 cs392_shell: cs392_log.c file
Course: CS 392 Systems Programming
*/
/*This file will contain the functions to do the logging*/
#include<stdio.h>
#include<stdlib.h>
#include<errno.h>
#include"cs392_log.h"

void log_input(char* line){
    //Function to write the input into log file
    //Open the file in appending mode
    //Creates the file if it doesn't exist
    FILE* fp = fopen("cs392_shell.log", "a");
    
    //Check if the file was opened
    if(fp == NULL){
        fprintf(stderr, "Error (%d): Cannot open file\n", errno);
        exit(1);
    }
    //Place the input line in the file
    fprintf(fp, "%s\n", line);
    //Close the file
    fclose(fp);
}
