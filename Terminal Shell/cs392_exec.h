/*
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
Author: Dave Taveras
Date: May 3rd, 2020
Assignment: HW3 cs392_shell: cs392_exec.h file
Course: CS 392 Systems Programming
*/

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/wait.h>

#ifndef CS392_EXEC_H
#define CS392_EXEC_H
char* read_input(char* buf);
void execute_commands(char* line);
#endif
