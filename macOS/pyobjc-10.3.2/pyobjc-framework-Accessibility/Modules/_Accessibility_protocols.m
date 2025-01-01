/*
 * This file is generated by objective.metadata
 *
 * Last update: Wed Jan 16 13:10:52 2013
 */

static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p;
#if PyObjC_BUILD_RELEASE >= 1016
    p = PyObjC_IdToPython(@protocol(AXCustomContentProvider));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1200
    p = PyObjC_IdToPython(@protocol(AXChart));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(AXDataAxisDescriptor));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1201
    p = PyObjC_IdToPython(@protocol(AXBrailleMapRenderer));
    Py_XDECREF(p);
#endif
}
