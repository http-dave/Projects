This project was an assignment from my Systems Programming class at Stevens. 

This project utilizies the language C and practices involving writing headers for methods, writing a makefile to link, and compile all nessesary files and executables, and using signal handlers to catch interruption commands like ctrl c.

When running the program mimics a linux terminal shell. It takes UNIX commands that would be run through a terminal and executes them using the execvp() function. As currently implemented only one pipe is allowed to combine two commands.
