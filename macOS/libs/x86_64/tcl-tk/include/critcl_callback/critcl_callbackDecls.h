#ifndef critcl_callback_DECLS_H
#define critcl_callback_DECLS_H

#include <tcl.h>

#include "callback.h"
/*
 * These macros are used to control whether functions are being declared for
 * import or export. If a function is being declared while it is being built
 * to be included in a shared library, then it should have the DLLEXPORT
 * storage class. If is being declared for use by a module that is going to
 * link against the shared library, then it should have the DLLIMPORT storage
 * class. If the symbol is beind declared for a static build or for use from a
 * stub library, then the storage class should be empty.
 *
 * The convention is that a macro called BUILD_xxxx, where xxxx is the name of
 * a library we are building, is set on the compile line for sources that are
 * to be placed in the library. When this macro is set, the storage class will
 * be set to DLLEXPORT. At the end of the header file, the storage class will
 * be reset to DLLIMPORT.
 */

#undef TCL_STORAGE_CLASS
#ifdef BUILD_critcl_callback
#   define TCL_STORAGE_CLASS DLLEXPORT
#else
#   ifdef USE_CRITCL_CALLBACK_STUBS
#      define TCL_STORAGE_CLASS
#   else
#      define TCL_STORAGE_CLASS DLLIMPORT
#   endif
#endif


/*
 * Exported function declarations:
 */

/* 0 */
EXTERN critcl_callback_p critcl_callback_new(Tcl_Interp*interp,
				Tcl_Size objc, Tcl_Obj**objv, Tcl_Size nargs);
/* 1 */
EXTERN void		critcl_callback_extend(critcl_callback_p callback,
				Tcl_Obj*argument);
/* 2 */
EXTERN void		critcl_callback_destroy(critcl_callback_p callback);
/* 3 */
EXTERN int		critcl_callback_invoke(critcl_callback_p callback,
				Tcl_Size objc, Tcl_Obj**objv);

typedef struct Critcl_callbackStubs {
    int magic;
    const struct Critcl_callbackStubHooks *hooks;

    critcl_callback_p (*critcl_callback_new) (Tcl_Interp*interp, Tcl_Size objc, Tcl_Obj**objv, Tcl_Size nargs); /* 0 */
    void (*critcl_callback_extend) (critcl_callback_p callback, Tcl_Obj*argument); /* 1 */
    void (*critcl_callback_destroy) (critcl_callback_p callback); /* 2 */
    int (*critcl_callback_invoke) (critcl_callback_p callback, Tcl_Size objc, Tcl_Obj**objv); /* 3 */
} Critcl_callbackStubs;

#ifdef __cplusplus
extern "C" {
#endif
extern const Critcl_callbackStubs *critcl_callbackStubsPtr;
#ifdef __cplusplus
}
#endif

#if defined(USE_CRITCL_CALLBACK_STUBS)

/*
 * Inline function declarations:
 */

#define critcl_callback_new \
	(critcl_callbackStubsPtr->critcl_callback_new) /* 0 */
#define critcl_callback_extend \
	(critcl_callbackStubsPtr->critcl_callback_extend) /* 1 */
#define critcl_callback_destroy \
	(critcl_callbackStubsPtr->critcl_callback_destroy) /* 2 */
#define critcl_callback_invoke \
	(critcl_callbackStubsPtr->critcl_callback_invoke) /* 3 */

#endif /* defined(USE_CRITCL_CALLBACK_STUBS) */
#endif /* critcl_callback_DECLS_H */

