# sha256c.decls -- -*- tcl -*-
#
#	This file contains the declarations for all public functions
#	that are exported by the "sha256c" library via its stubs table.
#

library   sha256c

interface sha256c

declare 0 generic {
    void SHA256Init (SHA256Context * sc)
}

declare 1 generic {
    void SHA256Update (SHA256Context * sc, const void * data, uint32_t len)
}

declare 2 generic {
    void SHA256Final (SHA256Context * sc, uint8_t * hash)
}

# END sha256c
