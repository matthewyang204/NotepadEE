# tclConfig.sh --
#
# This shell script (for sh) is generated automatically by Tcl's
# configure script.  It will create shell variables for most of
# the configuration options discovered by the configure script.
# This script is intended to be included by the configure scripts
# for Tcl extensions so that they don't have to figure this all
# out for themselves.
#
# The information in this file is specific to a single platform.

# Tcl's version number.
TCL_VERSION='9.0'
TCL_MAJOR_VERSION='9'
TCL_MINOR_VERSION='0'
TCL_PATCH_LEVEL='.1'

# C compiler to use for compilation.
TCL_CC='clang'

# -D flags for use with the C compiler.
TCL_DEFS='-DPACKAGE_NAME=\"tcl\" -DPACKAGE_TARNAME=\"tcl\" -DPACKAGE_VERSION=\"9.0\" -DPACKAGE_STRING=\"tcl\ 9.0\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE_URL=\"\" -DHAVE_STDIO_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_STRINGS_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_UNISTD_H=1 -DHAVE_SYS_TIME_H=1 -DSTDC_HEADERS=1 -DHAVE_SYS_PARAM_H=1 -DTCL_CFGVAL_ENCODING=\"utf-8\" -D_REENTRANT=1 -D_THREAD_SAFE=1 -DHAVE_PTHREAD_ATTR_SETSTACKSIZE=1 -DHAVE_PTHREAD_ATFORK=1 -DHAVE_DECL_PTHREAD_MUTEX_RECURSIVE=1 -DTCL_WITH_EXTERNAL_TOMMATH=1 -DMODULE_SCOPE=extern\ __attribute__\(\(__visibility__\(\"hidden\"\)\)\) -DHAVE_HIDDEN=1 -DMAC_OSX_TCL=1 -DHAVE_COREFOUNDATION=1 -DTCL_CFG_DO64BIT=1 -DHAVE_CAST_TO_UNION=1 -DHAVE_STDBOOL_H=1 -DHAVE_VFORK=1 -DHAVE_POSIX_SPAWNP=1 -DHAVE_POSIX_SPAWN_FILE_ACTIONS_ADDDUP2=1 -DHAVE_POSIX_SPAWNATTR_SETFLAGS=1 -DTCL_SHLIB_EXT=\".dylib\" -DNDEBUG=1 -DTCL_CFG_OPTIMIZED=1 -DMP_PREC=4 -DTCL_WIDE_INT_IS_LONG=1 -DHAVE_GETCWD=1 -DHAVE_MKSTEMP=1 -DHAVE_WAITPID=1 -DHAVE_GETNAMEINFO=1 -DHAVE_GETADDRINFO=1 -DHAVE_FREEADDRINFO=1 -DHAVE_GAI_STRERROR=1 -DHAVE_STRUCT_ADDRINFO=1 -DHAVE_STRUCT_IN6_ADDR=1 -DHAVE_STRUCT_SOCKADDR_IN6=1 -DHAVE_STRUCT_SOCKADDR_STORAGE=1 -DHAVE_GETPWUID_R_5=1 -DHAVE_GETPWUID_R=1 -DHAVE_GETPWNAM_R_5=1 -DHAVE_GETPWNAM_R=1 -DHAVE_GETGRGID_R_5=1 -DHAVE_GETGRGID_R=1 -DHAVE_GETGRNAM_R_5=1 -DHAVE_GETGRNAM_R=1 -DHAVE_MTSAFE_GETHOSTBYNAME=1 -DHAVE_MTSAFE_GETHOSTBYADDR=1 -DHAVE_TERMIOS_H=1 -DHAVE_SYS_IOCTL_H=1 -DHAVE_SYS_TIME_H=1 -DHAVE_GMTIME_R=1 -DHAVE_LOCALTIME_R=1 -DHAVE_TM_GMTOFF=1 -DHAVE_TIMEZONE_VAR=1 -DHAVE_STRUCT_STAT_ST_BLOCKS=1 -DHAVE_STRUCT_STAT_ST_BLKSIZE=1 -DHAVE_STRUCT_STAT_ST_RDEV=1 -DHAVE_BLKCNT_T=1 -DHAVE_INTPTR_T=1 -DHAVE_UINTPTR_T=1 -DHAVE_SIGNED_CHAR=1 -DHAVE_LANGINFO=1 -DHAVE_CFMAKERAW=1 -DHAVE_CHFLAGS=1 -DHAVE_MKSTEMPS=1 -DHAVE_GETATTRLIST=1 -DHAVE_COPYFILE_H=1 -DHAVE_COPYFILE=1 -DHAVE_LIBKERN_OSATOMIC_H=1 -DHAVE_OSSPINLOCKLOCK=1 -DTCL_LOAD_FROM_MEMORY=1 -DTCL_WIDE_CLICKS=1 -DHAVE_WEAK_IMPORT=1 -D_DARWIN_C_SOURCE=1 -DHAVE_FTS=1 -DHAVE_SYS_IOCTL_H=1 -DHAVE_SYS_FILIO_H=1 -DTCL_UNLOAD_DLLS=1'

# Default flags used in an optimized and debuggable build, respectively.
TCL_CFLAGS_DEBUG='-g'
TCL_CFLAGS_OPTIMIZE='-O2'

# Default linker flags used in an optimized and debuggable build, respectively.
TCL_LDFLAGS_DEBUG=''
TCL_LDFLAGS_OPTIMIZE=''

# Flag, 1: we built a shared lib, 0 we didn't
TCL_SHARED_BUILD=1

# The name of the Tcl library (may be either a .a file or a shared library):
TCL_LIB_FILE='libtcl9.0.dylib'

# The name of a zip containing the /library and /encodings (may be either a .zip file or a shared library):
TCL_ZIP_FILE=''

# Additional libraries to use when linking Tcl.
TCL_LIBS=' -lz  -lpthread -framework CoreFoundation  -ltommath'

# Top-level directory in which Tcl's platform-independent files are
# installed.
TCL_PREFIX='/opt/homebrew/Cellar/tcl-tk/9.0.1'

# Top-level directory in which Tcl's platform-specific files (e.g.
# executables) are installed.
TCL_EXEC_PREFIX='/opt/homebrew/Cellar/tcl-tk/9.0.1'

# Flags to pass to cc when compiling the components of a shared library:
TCL_SHLIB_CFLAGS='-fno-common'

# Flags to pass to cc to get warning messages
TCL_CFLAGS_WARNING='-Wall -Wextra -Wshadow -Wundef -Wwrite-strings -Wpointer-arith -Wc++-compat -fextended-identifiers'

# Extra flags to pass to cc:
TCL_EXTRA_CFLAGS='-pipe  -arch arm64 -finput-charset=UTF-8  '

# Base command to use for combining object files into a shared library:
TCL_SHLIB_LD='${CC} -dynamiclib ${CFLAGS} ${LDFLAGS}'

# Base command to use for combining object files into a static library:
TCL_STLIB_LD='${AR} cr'

# Either '$LIBS' (if dependent libraries should be included when linking
# shared libraries) or an empty string.  See Tcl's configure.ac for more
# explanation.
TCL_SHLIB_LD_LIBS='${LIBS}'

# Suffix to use for the name of a shared library.
TCL_SHLIB_SUFFIX='.dylib'

# Library file(s) to include in tclsh and other base applications
# in order to provide facilities needed by DLOBJ above.
TCL_DL_LIBS=''

# Flags to pass to the compiler when linking object files into
# an executable tclsh or tcltest binary.
TCL_LD_FLAGS=' -headerpad_max_install_names -Wl,-search_paths_first '

# Flags to pass to cc/ld, such as "-R /usr/local/tcl/lib", that tell the
# run-time dynamic linker where to look for shared libraries such as
# libtcl.so.  Used when linking applications.  Only works if there
# is a variable "LIB_RUNTIME_DIR" defined in the Makefile.
TCL_CC_SEARCH_FLAGS=''
TCL_LD_SEARCH_FLAGS=''

# Additional object files linked with Tcl to provide compatibility
# with standard facilities from ANSI C or POSIX.
TCL_COMPAT_OBJS=''

# Name of the ranlib program to use.
TCL_RANLIB='ranlib'

# -l flag to pass to the linker to pick up the Tcl library
TCL_LIB_FLAG='-ltcl9.0'

# String to pass to linker to pick up the Tcl library from its
# build directory.
TCL_BUILD_LIB_SPEC='-L/private/tmp/tcl-tk-20250112-6051-w9rb2k/tcl9.0.1/unix -ltcl9.0'

# String to pass to linker to pick up the Tcl library from its
# installed directory.
TCL_LIB_SPEC='-L/opt/homebrew/Cellar/tcl-tk/9.0.1/lib -ltcl9.0'

# String to pass to the compiler so that an extension can
# find installed Tcl headers.
TCL_INCLUDE_SPEC='-I/opt/homebrew/Cellar/tcl-tk/9.0.1/include/tcl-tk'

# Indicates whether a version numbers should be used in -l switches
# ("ok" means it's safe to use switches like -ltcl7.5;  "nodots" means
# use switches like -ltcl75).  SunOS and FreeBSD require "nodots", for
# example.
TCL_LIB_VERSIONS_OK='ok'

# String that can be evaluated to generate the part of a shared library
# name that comes after the "libxxx" (includes version number, if any,
# extension, and anything else needed).  May depend on the variables
# VERSION and SHLIB_SUFFIX.  On most UNIX systems this is
# ${VERSION}${SHLIB_SUFFIX}.
TCL_SHARED_LIB_SUFFIX='${VERSION}.dylib'

# String that can be evaluated to generate the part of an unshared library
# name that comes after the "libxxx" (includes version number, if any,
# extension, and anything else needed).  May depend on the variable
# VERSION.  On most UNIX systems this is ${VERSION}.a.
TCL_UNSHARED_LIB_SUFFIX='${VERSION}.a'

# Location of the top-level source directory from which Tcl was built.
# This is the directory that contains a README file as well as
# subdirectories such as generic, unix, etc.  If Tcl was compiled in a
# different place than the directory containing the source files, this
# points to the location of the sources, not the location where Tcl was
# compiled.
TCL_SRC_DIR='/private/tmp/tcl-tk-20250112-6051-w9rb2k/tcl9.0.1'

# List of standard directories in which to look for packages during
# "package require" commands.  Contains the "prefix" directory plus also
# the "exec_prefix" directory, if it is different.
TCL_PACKAGE_PATH='/opt/homebrew/lib'

# Tcl supports stub.
TCL_SUPPORTS_STUBS=1

# The name of the Tcl stub library (.a):
TCL_STUB_LIB_FILE='libtclstub.a'

# -l flag to pass to the linker to pick up the Tcl stub library
TCL_STUB_LIB_FLAG='-ltclstub'

# String to pass to linker to pick up the Tcl stub library from its
# build directory.
TCL_BUILD_STUB_LIB_SPEC='-L/private/tmp/tcl-tk-20250112-6051-w9rb2k/tcl9.0.1/unix -ltclstub'

# String to pass to linker to pick up the Tcl stub library from its
# installed directory.
TCL_STUB_LIB_SPEC='-L/opt/homebrew/Cellar/tcl-tk/9.0.1/lib -ltclstub'

# Path to the Tcl stub library in the build directory.
TCL_BUILD_STUB_LIB_PATH='/private/tmp/tcl-tk-20250112-6051-w9rb2k/tcl9.0.1/unix/libtclstub.a'

# Path to the Tcl stub library in the install directory.
TCL_STUB_LIB_PATH='/opt/homebrew/Cellar/tcl-tk/9.0.1/lib/libtclstub.a'
