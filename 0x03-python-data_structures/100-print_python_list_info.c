#include "/usr/include/python3.8/Python.h"
#include <stdio.h>

/**
 * print_python_list_info - print python info
 * @p: pyobject
 *
 * Return: none.
 */

void print_python_list_info(PyObject *p)
{
	int i;
	int list_len = 0;
	PyObject *item;
	PyListObject *clone = (PyListObject *) p;

	list_len = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", list_len);
	printf("[*] Allocated = %d\n", (int) clone->allocated);

	for (i = 0; i < list_len; ++i)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
	}
    return;
}

