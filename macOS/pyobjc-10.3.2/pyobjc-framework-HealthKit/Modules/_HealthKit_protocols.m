/*
 * This file is generated by objective.metadata
 *
 * Last update: Wed Jun 22 22:20:18 2022
 */

static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if PyObjC_BUILD_RELEASE >= 1300
    p = PyObjC_IdToPython(@protocol(HKLiveWorkoutBuilderDelegate));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(HKWorkoutSessionDelegate));
    Py_XDECREF(p);
#endif /* PyObjC_BUILD_RELEASE >= 1300 */
}
