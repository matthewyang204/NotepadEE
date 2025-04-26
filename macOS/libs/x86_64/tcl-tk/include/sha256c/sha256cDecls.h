#ifndef sha256c_DECLS_H
#define sha256c_DECLS_H

#include <tcl.h>

#include "sha256.h"
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
#ifdef BUILD_sha256c
#   define TCL_STORAGE_CLASS DLLEXPORT
#else
#   ifdef USE_SHA256C_STUBS
#      define TCL_STORAGE_CLASS
#   else
#      define TCL_STORAGE_CLASS DLLIMPORT
#   endif
#endif


/*
 * Exported function declarations:
 */

/* 0 */
EXTERN void		SHA256Init(SHA256Context *sc);
/* 1 */
EXTERN void		SHA256Update(SHA256Context *sc, const void *data,
				uint32_t len);
/* 2 */
EXTERN void		SHA256Final(SHA256Context *sc, uint8_t *hash);

typedef struct Sha256cStubs {
    int magic;
    const struct Sha256cStubHooks *hooks;

    void (*sHA256Init) (SHA256Context *sc); /* 0 */
    void (*sHA256Update) (SHA256Context *sc, const void *data, uint32_t len); /* 1 */
    void (*sHA256Final) (SHA256Context *sc, uint8_t *hash); /* 2 */
} Sha256cStubs;

#ifdef __cplusplus
extern "C" {
#endif
extern const Sha256cStubs *sha256cStubsPtr;
#ifdef __cplusplus
}
#endif

#if defined(USE_SHA256C_STUBS)

/*
 * Inline function declarations:
 */

#define SHA256Init \
	(sha256cStubsPtr->sHA256Init) /* 0 */
#define SHA256Update \
	(sha256cStubsPtr->sHA256Update) /* 1 */
#define SHA256Final \
	(sha256cStubsPtr->sHA256Final) /* 2 */

#endif /* defined(USE_SHA256C_STUBS) */
#endif /* sha256c_DECLS_H */

