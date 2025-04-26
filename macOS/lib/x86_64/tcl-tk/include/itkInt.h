/*
 * ------------------------------------------------------------------------
 *      PACKAGE:  [incr Tk]
 *  DESCRIPTION:  Building mega-widgets with [incr Tcl]
 *
 *  [incr Tk] provides a framework for building composite "mega-widgets"
 *  using [incr Tcl] classes.  It defines a set of base classes that are
 *  specialized to create all other widgets.
 *
 *
 * ========================================================================
 *  AUTHOR:  Michael J. McLennan
 *           Bell Labs Innovations for Lucent Technologies
 *           mmclennan@lucent.com
 *           http://www.tcltk.com/itcl
 * ========================================================================
 *           Copyright (c) 1993-1998  Lucent Technologies, Inc.
 * ------------------------------------------------------------------------
 * See the file "license.terms" for information on usage and redistribution
 * of this file, and for a DISCLAIMER OF ALL WARRANTIES.
 */

#include <itclInt.h>
#include "itk.h"

/*
 *  List of options in alphabetical order:
 */
typedef struct ItkOptList {
    Tcl_HashTable *options;     /* list containing the real options */
    Tcl_HashEntry **list;       /* gives ordering of options */
    int len;                    /* number of entries in order list */
    int max;                    /* maximum size of order list */
} ItkOptList;

/*
 *  List of options created in the class definition:
 */
typedef struct ItkClassOptTable {
    Tcl_HashTable options;        /* option storage with fast lookup */
    ItkOptList order;             /* gives ordering of options */
} ItkClassOptTable;

/*
 *  Each option created in the class definition:
 */
typedef struct ItkClassOption {
    Tcl_Obj* namePtr;           /* member name */
    Tcl_Obj* fullNamePtr;       /* member name with "class::" qualifier */
    ItclClass* iclsPtr;         /* class containing this member */
    int protection;             /* protection level */
    int flags;                  /* flags describing member (see above) */
    ItclMemberCode *codePtr;    /* code associated with member */
    char *resName;                /* resource name in X11 database */
    char *resClass;               /* resource class name in X11 database */
    char *init;                   /* initial value for option */
} ItkClassOption;


/*
 *  Info associated with each Archetype mega-widget:
 */
typedef struct ArchInfo {
    ItclObject *itclObj;        /* object containing this info */
    Tk_Window tkwin;            /* window representing this mega-widget */
    Tcl_HashTable components;   /* list of all mega-widget components */
    Tcl_HashTable options;      /* list of all mega-widget options */
    ItkOptList order;           /* gives ordering of options */
} ArchInfo;

/*
 *  Each component widget in an Archetype mega-widget:
 */
typedef struct ArchComponent {
    Tcl_Obj* namePtr;           /* member name */
    Tcl_Obj* fullNamePtr;       /* member name with "class::" qualifier */
    ItclClass* iclsPtr;         /* class containing this member */
    int protection;             /* protection level */
    int flags;                  /* flags describing member (see above) */
    ItclMemberCode *codePtr;    /* code associated with member */
    Tcl_Command accessCmd;      /* access command for component widget */
    Tk_Window tkwin;            /* Tk window for this component widget */
    char *pathName;             /* Tk path name for this component widget.
                                   We can't use the tkwin pointer after
                                   the window has been destroyed so we
                                   need to save a copy for use in
                                   Itk_ArchCompDeleteCmd() */
} ArchComponent;

/*
 *  Each option in an Archetype mega-widget:
 */
typedef struct ArchOption {
    char *switchName;           /* command-line switch for this option */
    char *resName;              /* resource name in X11 database */
    char *resClass;             /* resource class name in X11 database */
    char *init;                 /* initial value for option */
    int flags;                  /* flags representing option state */
    Itcl_List parts;            /* parts relating to this option */
} ArchOption;

/*
 *  Flag bits for ArchOption state:
 */
#define ITK_ARCHOPT_INIT  0x01  /* option has been initialized */

/*
 *  Various parts of a composite option in an Archetype mega-widget:
 */
typedef int (Itk_ConfigOptionPartProc) (Tcl_Interp *interp,
    ItclObject *contextObj, void *cdata, const char* newVal);

typedef struct ArchOptionPart {
    void *clientData;                 /* data associated with this part */
    Itk_ConfigOptionPartProc *configProc;  /* update when new vals arrive */
    Tcl_CmdDeleteProc *deleteProc;         /* clean up after clientData */

    void *from;                       /* token that indicates who
                                            * contributed this option part */
} ArchOptionPart;


/*
 *  Info kept by the itk::option-parser namespace and shared by
 *  all option processing commands:
 */
typedef struct ArchMergeInfo {
    Tcl_HashTable usualCode;      /* usual option handling code for the
                                   * various widget classes */

    ArchInfo *archInfo;           /* internal option info for mega-widget */
    ArchComponent *archComp;      /* component being merged into mega-widget */
    Tcl_HashTable *optionTable;   /* table of valid configuration options
                                   * for component being merged */
} ArchMergeInfo;

/*
 *  Used to capture component widget configuration options when a
 *  new component is being merged into a mega-widget:
 */
typedef struct GenericConfigOpt {
    char *switchName;             /* command-line switch for this option */
    char *resName;                /* resource name in X11 database */
    char *resClass;               /* resource class name in X11 database */
    char *init;                   /* initial value for this option */
    char *value;                  /* current value for this option */
    char **storage;               /* storage for above strings */

    ArchOption *integrated;       /* integrated into this mega-widget option */
    ArchOptionPart *optPart;      /* integrated as this option part */
} GenericConfigOpt;

/*
 *  Options that are propagated by a "configure" method:
 */
typedef struct ConfigCmdline {
    Tcl_Obj *objv[4];           /* objects representing "configure" command */
} ConfigCmdline;

MODULE_SCOPE int Itk_ArchInitOptsCmd (void *cdata,
    Tcl_Interp *interp, int objc, Tcl_Obj *const objv[]);
MODULE_SCOPE int Itk_ArchDeleteOptsCmd (void *cdata,
    Tcl_Interp *interp, int objc, Tcl_Obj *const objv[]);
MODULE_SCOPE int Itk_ArchComponentCmd (void *cdata,
    Tcl_Interp *interp, int objc, Tcl_Obj *const objv[]);
MODULE_SCOPE int Itk_ArchInitCmd (void *cdata,
    Tcl_Interp *interp, int objc, Tcl_Obj *const objv[]);
MODULE_SCOPE int Itk_ArchOptionCmd (void *cdata,
    Tcl_Interp *interp, int objc, Tcl_Obj *const objv[]);
MODULE_SCOPE int Itk_ArchCompAccessCmd (void *cdata,
    Tcl_Interp *interp, int objc, Tcl_Obj *const objv[]);
MODULE_SCOPE int Itk_ArchConfigureCmd (void *cdata,
    Tcl_Interp *interp, int objc, Tcl_Obj *const objv[]);
MODULE_SCOPE int Itk_ArchCgetCmd (void *cdata,
    Tcl_Interp *interp, int objc, Tcl_Obj *const objv[]);

MODULE_SCOPE int Itk_ArchCompAddCmd (void *cdata,
    Tcl_Interp *interp, int objc, Tcl_Obj *const objv[]);
MODULE_SCOPE int Itk_ArchCompDeleteCmd (void *cdata,
    Tcl_Interp *interp, int objc, Tcl_Obj *const objv[]);
MODULE_SCOPE int Itk_ArchConfigOption (Tcl_Interp *interp,
    ArchInfo *info, char *name, char *value);
MODULE_SCOPE int Itk_ArchOptionAddCmd (void *cdata,
    Tcl_Interp *interp, int objc, Tcl_Obj *const objv[]);
MODULE_SCOPE int Itk_ArchOptionRemoveCmd (void *cdata,
    Tcl_Interp *interp, int objc, Tcl_Obj *const objv[]);
MODULE_SCOPE int Itk_PropagatePublicVar (Tcl_Interp *interp,
    ItclObject *contextObj, void *cdata, const char *newval);
MODULE_SCOPE int Itk_GetArchInfo (Tcl_Interp *interp,
    ItclObject* contextObj, ArchInfo **infoPtr);
MODULE_SCOPE void Itk_ArchOptConfigError (Tcl_Interp *interp,
    ArchInfo *info, ArchOption *archOpt);
MODULE_SCOPE void Itk_ArchOptAccessError (Tcl_Interp *interp,
    ArchInfo *info, ArchOption *archOpt);
MODULE_SCOPE ArchOptionPart* Itk_CreateOptionPart (
    Tcl_Interp *interp, void *cdata, Itk_ConfigOptionPartProc* cproc,
    Tcl_CmdDeleteProc *dproc, void *from);
MODULE_SCOPE int Itk_AddOptionPart (Tcl_Interp *interp,
    ArchInfo *info, char *switchName, char *resName, char *resClass,
    const char *defVal, char *currVal, ArchOptionPart *optPart,
    ArchOption **raOpt);
MODULE_SCOPE ArchOptionPart* Itk_FindArchOptionPart (
    ArchInfo *info, char *switchName, void *from);
MODULE_SCOPE void Itk_DelOptionPart (ArchOptionPart *optPart);
MODULE_SCOPE void Itk_DelArchInfo (void *cdata);
MODULE_SCOPE Tcl_HashTable* ItkGetObjsWithArchInfo
    (Tcl_Interp *interp);
MODULE_SCOPE void ItkFreeObjsWithArchInfo (void *cdata,
    Tcl_Interp *interp);
MODULE_SCOPE void Itk_DelMergeInfo (void* cdata);
MODULE_SCOPE int Itk_ArchOptKeepCmd (void *cdata,
    Tcl_Interp *interp, int objc, Tcl_Obj *const objv[]);
MODULE_SCOPE int Itk_ArchOptIgnoreCmd (void *cdata,
    Tcl_Interp *interp, int objc, Tcl_Obj *const objv[]);
MODULE_SCOPE int Itk_ArchOptRenameCmd (void *cdata,
    Tcl_Interp *interp, int objc, Tcl_Obj *const objv[]);
MODULE_SCOPE int Itk_ArchOptUsualCmd (void *cdata,
    Tcl_Interp *interp, int objc, Tcl_Obj *const objv[]);


#include "itkIntDecls.h"
