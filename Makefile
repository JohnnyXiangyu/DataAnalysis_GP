cc=gcc
flags=-Wall -Wextra -fPIC -g -shared
pyflags=-I/usr/include/python3.6 -I/usr/lib/python3.6/config

Stdin_Input: Stdin_Input.c 
	$(cc) Stdin_Input.c -o Stdin_Input.so $(flags) $(pyflags)

example: PyExample.c
	$(cc) PyExample.c -o example.so $(flags) $(pyflags)

clean:
	rm -f *.so
