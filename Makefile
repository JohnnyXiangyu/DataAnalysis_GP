cc=gcc
flags=-Wall -Wextra -fPIC -g -shared

Stdin_Input: Stdin_Input.c 
	$(cc) Stdin_Input.c -o example.so $(flags) -I/usr/include/python2.6 -I/usr/lib/python2.6/config
