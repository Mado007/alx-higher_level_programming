#include <Python.h>
#include <listobject.h>
#include <object.h>


void print_python_list_info(PyObject *p)
{
long int size = PyList_Size(p);
int d;
PyListObject *obj = (PyListObject *)p;

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", obj->allocated);
for (d = 0; d < size; d++)
printf("Element %d: %s\n", d, Py_TYPE(obj->ob_item[d])->tp_name);
}
