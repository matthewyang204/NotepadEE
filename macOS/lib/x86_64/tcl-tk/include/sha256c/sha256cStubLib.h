
/*
 * sha256cStubLib.c --
 *
 * Stub object that will be statically linked into extensions that wish
 * to access sha256c.
 */

/*
 * We need to ensure that we use the stub macros so that this file contains
 * no references to any of the stub functions.  This will make it possible
 * to build an extension that references Sha256c_InitStubs but doesn't end up
 * including the rest of the stub functions.
 */

#ifndef USE_TCL_STUBS
#define USE_TCL_STUBS
#endif
#undef  USE_TCL_STUB_PROCS

#include <tcl.h>

#ifndef USE_SHA256C_STUBS
#define USE_SHA256C_STUBS
#endif
#undef  USE_SHA256C_STUB_PROCS

#include "sha256cDecls.h"

/*
 * Ensure that Sha256c_InitStubs is built as an exported symbol.  The other stub
 * functions should be built as non-exported symbols.
 */

#undef  TCL_STORAGE_CLASS
#define TCL_STORAGE_CLASS DLLEXPORT

const Sha256cStubs* sha256cStubsPtr;


/*
 *----------------------------------------------------------------------
 *
 * Sha256c_InitStubs --
 *
 * Checks that the correct version of Sha256c is loaded and that it
 * supports stubs. It then initialises the stub table pointers.
 *
 * Results:
 *  The actual version of Sha256c that satisfies the request, or
 *  NULL to indicate that an error occurred.
 *
 * Side effects:
 *  Sets the stub table pointers.
 *
 *----------------------------------------------------------------------
 */

#ifdef Sha256c_InitStubs
#undef Sha256c_InitStubs
#endif

char *
Sha256c_InitStubs(Tcl_Interp *interp, CONST char *version, int exact)
{
    CONST char *actualVersion;

    actualVersion = Tcl_PkgRequireEx(interp, "sha256c", version,
				     exact, (ClientData *) &sha256cStubsPtr);
    if (!actualVersion) {
	return NULL;
    }

    if (!sha256cStubsPtr) {
	Tcl_SetResult(interp,
		      "This implementation of Sha256c does not support stubs",
		      TCL_STATIC);
	return NULL;
    }
    
    return (char*) actualVersion;
}
    
