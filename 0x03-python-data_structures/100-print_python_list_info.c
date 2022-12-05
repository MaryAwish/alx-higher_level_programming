#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - prints info about python lists
 *
 * @p: pyobject pointer
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	long int size = Pylist_Size(p);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
