#include <stdio.h>
#include <python3.6m/Python.h>

int fact(int n)
{
    if (n <= 1)
        return 1;
    else
        return n * fact(n - 1);
}

PyObject *wrap_fact(PyObject *self, PyObject *args)
{
    int n, result;
    if (!PyArg_ParseTuple(args, "i:fact", &n))
    return NULL;
    result = fact(n);
    return Py_BuildValue("i", result);
}

static PyMethodDef exampleMethods[] =
{
    {"fact", wrap_fact, METH_VARARGS, "Caculate N!"},
    {NULL, NULL}
};

static PyModuleDef example[] =
{
    PyModuleDef_HEAD_INIT,
    "example", /* name of module */
    "",          /* module documentation, may be NULL */
    -1,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    exampleMethods
};

PyMODINIT_FUNC PyInit_example(void)
{
    return PyModule_Create(&example);
}
