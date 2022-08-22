/*
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
Author: Dave Taveras
Date: May 3rd, 2020
Assignment: HW3 cs392_shell: cs392_signal.h file
Course: CS 392 Systems Programming
*/

/*This file will contain functions to register the signal handler*/
#include<stdio.h>
#include<string.h>
#include<signal.h>
#include<unistd.h>
#include<stdlib.h>
#include"cs392_signal.h"

//From the slides
static void signal_reader(int sig, siginfo_t *siginfo, void* context){
    if(sig == SIGTSTP){
        //if control Z is entered
        printf("\nStop Signal Received\n");
        sleep(1); //Prevents constant pressing
    }
    
    if(sig == SIGINT){
        //if control C is entered
        printf("\nTermination Signal Received\n");
        exit(1);
    }
}

//From the slides
void signal_handler(){
    struct sigaction act;
        
    memset (&act, '\0', sizeof(act));
    act.sa_sigaction = &signal_reader;
    act.sa_flags = SA_SIGINFO;
        
    if((sigaction(SIGTSTP, &act ,NULL) < 0) || (sigaction(SIGINT, &act, NULL) < 0)){
        perror("Sigaction error.\n");
    }
}

