//#define MS_NO_COREDLL
#include <Python.h>
#include <iostream>

extern "C"
{
	void helloWorld();
}

// import
PyObject* ImportPythonModule( const char* a_pyModuleName )
{
	PyObject* pObjName= PyString_FromString(a_pyModuleName);
	PyObject* pModule = PyImport_Import(pObjName);
	if (!pModule)
    {
        PyErr_Print();
        std::cout << stderr << "Failed to load \" " << a_pyModuleName << "\"" << std::endl;
    }
    Py_DECREF(pObjName);
	return pModule;
}

// Get the function
PyObject* GetHandleToPythonFunction( PyObject* a_pModule, const char* a_pFunctionName )
{
	 PyObject* pFunction = PyObject_GetAttrString(a_pModule, a_pFunctionName);
    /* pFunc is a new reference */
    if( !(pFunction && PyCallable_Check(pFunction)) ) 
	{
        if (PyErr_Occurred())
        {
			PyErr_Print();
		}
        std::cout << stderr << "Cannot find function \"" << a_pFunctionName << "\"" << std::endl;
    }
	return pFunction;
}

// Call functions
PyObject* CallPythonFunction( PyObject* a_pyFunction, PyObject* a_pyFuncArguments)
{
	PyObject* pReturnValue = PyObject_CallObject( a_pyFunction, a_pyFuncArguments );
    if (pReturnValue == nullptr)
	{
		PyErr_Print();
		fprintf(stderr,"Call failed\n");
    }
	return pReturnValue;
}

PyObject* HelloWorld()
{
	helloWorld();
	Py_RETURN_NONE;
}

PyMethodDef AIE_Functions[] = 
{ 
	//{“Name”, “Address”, “?Arguments?”, “Description”} 
	{"HelloWorld",(PyCFunction)HelloWorld,METH_NOARGS,"Say hello."}, 
	{NULL, NULL, 0, NULL} 
	}; 

int main(int argc, char *argv[])
{
	static char* argv_01 = "C:\Python27";
	static char* argvv[1];
	Py_Initialize();
	
	//\=============================================================== 
	//\Add our current directory to the path lookup for Python imports 
	//\=============================================================== 
	argvv[0] = argv_01;
	PySys_SetArgv(argc, argv);


	PyObject* sysPath = PySys_GetObject((char*)"path"); 
	
	PyList_Append(sysPath, PyString_FromString("./scripts"));

	//\===================================================== 
	//\Import the AIE C Functions into Python so that we can 
	//\call them from there we will need to add "import AIE" 
	//\to any Python files that we wish to use these functions in 
	//\====================================================== 
	Py_InitModule("AIE", AIE_Functions);

	PyObject * pyModule = ImportPythonModule("helloworld");

	PyObject * pyTestHandle = GetHandleToPythonFunction(pyModule, "nice");

	PyObject * pyTestHandleB = GetHandleToPythonFunction(pyModule, "hello");

	PyObject * args = NULL;

	CallPythonFunction(pyTestHandle, args);

	float dude;

	PyObject* ReturnVal = CallPythonFunction(pyTestHandleB, args);

	if (!PyArg_ParseTuple(ReturnVal, "f", &dude)) 
	{ 
		std::cout << "Error. \n"; 
	} 
	Py_DECREF(ReturnVal);

	//std::cout << dude << "\n";

	std::cin.get();
	std::cin.get();

}

void helloWorld()
{
	printf( "Python is shit \n");
}