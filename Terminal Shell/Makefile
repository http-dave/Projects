cs392_shell: cs392_shell.o cs392_exec.o cs392_log.o cs392_signal.o
	gcc -o cs392_shell cs392_shell.o cs392_exec.o cs392_log.o cs392_signal.o
	
cs392_shell.o: cs392_shell.c
	gcc -c cs392_shell.c
	
cs392_exec.o: cs392_exec.c cs392_exec.h
	gcc -c cs392_exec.c
	
cs392_log.o: cs392_log.c cs392_log.h
	gcc -c cs392_log.c
	
cs392_signal.o: cs392_signal.c cs392_signal.h
	gcc -c cs392_signal.c

clean:
	rm cs392_shell cs392_shell.o cs392_exec.o cs392_log.o cs392_signal.o