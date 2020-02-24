#include <stdio.h>
#include <python3.6m/Python.h>
#include <stdlib.h>
#include <termios.h>
#include <unistd.h>
#include <getopt.h>
#include <sys/poll.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <errno.h>


// TODO: CAN I REALLY USE GLOBAL STORAGE IN HERE?
/* global variable */
struct pollfd fds; /* poll file descriptor, in this case just STDIN_FILENO */
char input_buffer[1024]; /* input buffer, char array */
struct termios old_setting, new_setting; /* terminal settings */


int fact(int n) {
    if (n <= 1)
        return 1;
    else
        return n * fact(n - 1);
}

PyObject *wrap_fact(PyObject *self, PyObject *args) {
    int n, result;
    if (!PyArg_ParseTuple(args, "i:fact", &n))
        return NULL;
    result = fact(n);
    return Py_BuildValue("i", result);
}


/* args: none
 * return: 0 on success, otherwise failure
 * function: change terminal setting to no-echo-back mode
 *           initialize poll fd
 */
int inputInit(void) {
    /* initialize poll fd */
    fds.fd = STDIN_FILENO;
    fds.events = POLLIN;
    
    /* initialize input_buffer */
    int i;
    for (i = 0; i < 1024; i++) {
        input_buffer[i] = 0;
    }

    // get current setting and create a modified new setting
    int rc = tcgetattr(0, &old_setting);
    if (rc == -1) { return -1; }
    new_setting = old_setting;
    new_setting.c_iflag = ISTRIP;
    new_setting.c_oflag = 0;
    new_setting.c_lflag = 0;
    // apply changes TODO: in the man page it says this call will return success 
        // whenever at least 1 change has been made, need to further check
    rc = tcsetattr(0, TCSANOW, &new_setting);
    if (rc == -1) { return -1; }

    return 0;
}
PyObject *wrap_inputInit(PyObject *self, PyObject *args) {
    int rc = inputInit();
    return Py_BuildValue("i", rc);
}


/* Method: getInput()
 * args: none
 * return: a string containing all input inside stdin at the moment
 * function: when called, poll() stdin for input, and return the first 1023 bytes in a string
 *           if there's no input, return empty string
 */
PyObject *wrap_getInput(PyObject *self, PyObject *args) {
    int rc = poll(&fds, 1, 0); // poll with immediate timeout
    if (rc > 0 && fds.revents & POLLIN) {
        rc = read(STDIN_FILENO, &input_buffer, 1023);
        input_buffer[rc] = '\0';
        return Py_BuildValue("s", input_buffer);
    }
    else {
        return Py_BuildValue("s", "");
    }
}


/* args: none
 * return: 0 on success, otherwise failure
 * function: flush stdin by performing a 1024 byte read, then change terminal setting to normal mode
 */
int inputFinalize(void) {
    int rc = tcsetattr(0, TCSANOW, &old_setting);
    if (rc == -1) 
        return -1;
    else 
        return 0;
    
}
PyObject *wrap_inputFinalize(PyObject *self, PyObject *args) {
    int rc = inputFinalize();
    return Py_BuildValue("i", rc);
}


static PyMethodDef Stdin_InputMethods[] = {
    {"fact", wrap_fact, METH_VARARGS, "Caculate N!"},
    {"getInput", wrap_getInput, METH_NOARGS, "Get the latest input(s) from keyboard, max 1023 bytes."},
    {"inputInit", wrap_inputInit, METH_NOARGS, "Initialize input module, must be called before calling getInput."},
    {"inputFinalize", wrap_inputFinalize, METH_NOARGS, "Finalize input module, must be called after usage of the module."},
    {NULL, NULL, NULL, NULL}
};

static PyModuleDef Stdin_Input = {
    PyModuleDef_HEAD_INIT,
    "Stdin_Input", /* name of module */
    "",        /* module documentation, may be NULL */
    -1,        /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    Stdin_InputMethods
};

PyMODINIT_FUNC PyInit_Stdin_Input(void) {
    return PyModule_Create(&Stdin_Input);
}
