# critcl::callback.decls -- -*- tcl -*-
#
#	This file contains the declarations for all public functions
#	that are exported by the "critcl::callback" library via its stubs table.
#

library   critcl::callback

interface critcl_callback

declare 0 generic {
    critcl_callback_p critcl_callback_new (Tcl_Interp* interp, Tcl_Size objc, Tcl_Obj** objv, Tcl_Size nargs)
}

declare 1 generic {
    void critcl_callback_extend (critcl_callback_p callback, Tcl_Obj* argument)
}

declare 2 generic {
    void critcl_callback_destroy (critcl_callback_p callback)
}

declare 3 generic {
    int critcl_callback_invoke (critcl_callback_p callback, Tcl_Size objc, Tcl_Obj** objv)
}

# END critcl::callback
