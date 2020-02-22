cc=g++
flags=-Wall -Wextra -fPic -g -shared
pyflags=-I/usr/include/python3.6 -lboost_python 

Stdin_Input: Stdin_Input.cpp
	$(cc) Stdin_Input.cpp -o Stdin_Input.so $(flags) $(pyflags)
	