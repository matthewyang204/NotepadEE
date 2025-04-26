
/*
 * critcl_callbackStubLib.c --
 *
 * Stub object that will be statically linked into extensions that wish
 * to access critcl_callback.
 */

/*
 * We need to ensure that we use the stub macros so that this file contains
 * no references to any of the stub functions.  This will make it possible
 * to build an extension that references Critcl_callback_InitStubs but doesn't end up
 * including the rest of the stub functions.
 */

#ifndef USE_TCL_STUBS
#define USE_TCL_STUBS
#endif
#undef  USE_TCL_STUB_PROCS

#include <tcl.h>

#ifndef USE_CRITCL_CALLBACK_STUBS
#define USE_CRITCL_CALLBACK_STUBS
#endif
#undef  USE_CRITCL_CALLBACK_STUB_PROCS

#include "critcl_callbackDecls.h"

/*
 * Ensure that Critcl_callback_InitStubs is built as an exported symbol.  The other stub
 * functions should be built as non-exported symbols.
 */

#undef  TCL_STORAGE_CLASS
#define TCL_STORAGE_CLASS DLLEXPORT

const Critcl_callbackStubs* critcl_callbackStubsPtr;


/*
 *----------------------------------------------------------------------
 *
 * Critcl_callback_InitStubs --
 *
 * Checks that the correct version of Critcl_callback is loaded and that it
 * supports stubs. It then initialises the stub table pointers.
 *
 * Results:
 *  The actual version of Critcl_callback that satisfies the request, or
 *  NULL to indicate that an error occurred.
 *
 * Side effects:
 *  Sets the stub table pointers.
 *
 *----------------------------------------------------------------------
 */

#ifdef Critcl_callback_InitStubs
#undef Critcl_callback_InitStubs
#endif

char *
Critcl_callback_InitStubs(Tcl_Interp *interp, CONST char *version, int exact)
{
    CONST char *actualVersion;

    actualVersion = Tcl_PkgRequireEx(interp, "critcl::callback", version,
				     exact, (ClientData *) &critcl_callbackStubsPtr);
    if (!actualVersion) {
	return NULL;
    }

    if (!critcl_callbackStubsPtr) {
	Tcl_SetResult(interp,
		      "This implementation of Critcl_callback does not support stubs",
		      TCL_STATIC);
	return NULL;
    }
    
    return (char*) actualVersion;
}
    
