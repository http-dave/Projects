/*
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
Author: Dave Taveras
Date: May 3rd, 2020
Assignment: HW3 cs392_shell: cs392_signal.h file
Course: CS 392 Systems Programming
*/

#include<stdio.h>
#include<string.h>
#include<signal.h>
#include<unistd.h>
#include<stdlib.h>

#ifndef CS392_SIGNAL_H
#define CS392_SIGNAL_H
static void signal_reader(int sig, siginfo_t* siginfo, void* context);
void signal_handler();
#endif
