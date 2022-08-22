/*
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
Author: Dave Taveras
Date: May 3rd, 2020
Assignment: HW3 cs392_shell: cs392_shell.c file
Course: CS 392 Systems Programming
*/


/*This file will contain the main fucntions to implement the main logic*/
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include"cs392_exec.h"
#include"cs392_log.h"
#include"cs392_signal.h"
int main (int argc, char** argv){
    char line[1024]; // buffer for input
    int stat;
    
    do{
        signal_handler(); //run the signal handeler
        
        printf("cs392_shell $: "); //print the indicator
        
        fflush(stdout); //make sure the indicator prints
        
        read_input(line); //read an input from the user
        
        log_input(line); //log the input into the log file
        
        execute_commands(line); //execute the command
        
    }while(stat);
    return 0;
}


