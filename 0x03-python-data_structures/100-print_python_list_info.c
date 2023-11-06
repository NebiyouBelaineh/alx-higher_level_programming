#include <Python.h>
/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: is the Python Object list to be examined
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	long int index;
	PyObject *list_elem;
	PyListObject *list;

	printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (index = 0; index < Py_SIZE(p); index++)
	{
		list_elem = PyList_GetItem(p, index);
		printf("Element %ld: %s\n", index, Py_TYPE(list_elem)->tp_name);
	}

}
