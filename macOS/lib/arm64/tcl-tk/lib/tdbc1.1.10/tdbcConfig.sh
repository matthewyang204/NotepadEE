# tdbcConfig.sh --
#
# This shell script (for sh) is generated automatically by TDBC's configure
# script. It will create shell variables for most of the configuration options
# discovered by the configure script. This script is intended to be included
# by the configure scripts for TDBC extensions so that they don't have to
# figure this all out for themselves.
#
# The information in this file is specific to a single platform.
#
# RCS: @(#) $Id$

# TDBC's version number
tdbc_VERSION=1.1.10
TDBC_VERSION=1.1.10

# Name of the TDBC library - may be either a static or shared library
tdbc_LIB_FILE=libtcl9tdbc1.1.10.dylib
TDBC_LIB_FILE=libtcl9tdbc1.1.10.dylib

# String to pass to the linker to pick up the TDBC library from its build dir
tdbc_BUILD_LIB_SPEC="-L/private/tmp/tcl-tk-20250112-6051-w9rb2k/tcl9.0.1/unix/pkgs/tdbc1.1.10 -ltdbc1.1.10"
TDBC_BUILD_LIB_SPEC="-L/private/tmp/tcl-tk-20250112-6051-w9rb2k/tcl9.0.1/unix/pkgs/tdbc1.1.10 -ltdbc1.1.10"

# String to pass to the linker to pick up the TDBC library from its installed
# dir.
tdbc_LIB_SPEC="-L/opt/homebrew/Cellar/tcl-tk/9.0.1/lib/tdbc1.1.10 -ltdbc1.1.10"
TDBC_LIB_SPEC="-L/opt/homebrew/Cellar/tcl-tk/9.0.1/lib/tdbc1.1.10 -ltdbc1.1.10"

# Name of the TBDC stub library
tdbc_STUB_LIB_FILE="libtdbcstub.a"
TDBC_STUB_LIB_FILE="libtdbcstub.a"

# String to pass to the linker to pick up the TDBC stub library from its
# build directory
tdbc_BUILD_STUB_LIB_SPEC="-L/private/tmp/tcl-tk-20250112-6051-w9rb2k/tcl9.0.1/unix/pkgs/tdbc1.1.10 -ltdbcstub"
TDBC_BUILD_STUB_LIB_SPEC="-L/private/tmp/tcl-tk-20250112-6051-w9rb2k/tcl9.0.1/unix/pkgs/tdbc1.1.10 -ltdbcstub"

# String to pass to the linker to pick up the TDBC stub library from its
# installed directory
tdbc_STUB_LIB_SPEC="-L/opt/homebrew/Cellar/tcl-tk/9.0.1/lib/tdbc1.1.10 -ltdbcstub"
TDBC_STUB_LIB_SPEC="-L/opt/homebrew/Cellar/tcl-tk/9.0.1/lib/tdbc1.1.10 -ltdbcstub"

# Path name of the TDBC stub library in its build directory
tdbc_BUILD_STUB_LIB_PATH="/private/tmp/tcl-tk-20250112-6051-w9rb2k/tcl9.0.1/unix/pkgs/tdbc1.1.10/libtdbcstub.a"
TDBC_BUILD_STUB_LIB_PATH="/private/tmp/tcl-tk-20250112-6051-w9rb2k/tcl9.0.1/unix/pkgs/tdbc1.1.10/libtdbcstub.a"

# Path name of the TDBC stub library in its installed directory
tdbc_STUB_LIB_PATH="/opt/homebrew/Cellar/tcl-tk/9.0.1/lib/tdbc1.1.10/libtdbcstub.a"
TDBC_STUB_LIB_PATH="/opt/homebrew/Cellar/tcl-tk/9.0.1/lib/tdbc1.1.10/libtdbcstub.a"

# Location of the top-level source directories from which TDBC was built.
# This is the directory that contains doc/, generic/ and so on.  If TDBC
# was compiled in a directory other than the source directory, this still
# points to the location of the sources, not the location where TDBC was
# compiled.
tdbc_SRC_DIR="/private/tmp/tcl-tk-20250112-6051-w9rb2k/tcl9.0.1/pkgs/tdbc1.1.10"
TDBC_SRC_DIR="/private/tmp/tcl-tk-20250112-6051-w9rb2k/tcl9.0.1/pkgs/tdbc1.1.10"

# String to pass to the compiler so that an extension can find installed TDBC
# headers
tdbc_INCLUDE_SPEC="-I/opt/homebrew/Cellar/tcl-tk/9.0.1/include/tcl-tk"
TDBC_INCLUDE_SPEC="-I/opt/homebrew/Cellar/tcl-tk/9.0.1/include/tcl-tk"

# String to pass to the compiler so that an extension can find TDBC headers
# in the source directory
tdbc_BUILD_INCLUDE_SPEC="-I/private/tmp/tcl-tk-20250112-6051-w9rb2k/tcl9.0.1/pkgs/tdbc1.1.10/generic"
TDBC_BUILD_INCLUDE_SPEC="-I/private/tmp/tcl-tk-20250112-6051-w9rb2k/tcl9.0.1/pkgs/tdbc1.1.10/generic"

# Path name where .tcl files in the tdbc package appear at run time.
tdbc_LIBRARY_PATH="/opt/homebrew/Cellar/tcl-tk/9.0.1/lib/tdbc1.1.10"
TDBC_LIBRARY_PATH="/opt/homebrew/Cellar/tcl-tk/9.0.1/lib/tdbc1.1.10"

# Path name where .tcl files in the tdbc package appear at build time.
tdbc_BUILD_LIBRARY_PATH="/private/tmp/tcl-tk-20250112-6051-w9rb2k/tcl9.0.1/pkgs/tdbc1.1.10/library"
TDBC_BUILD_LIBRARY_PATH="/private/tmp/tcl-tk-20250112-6051-w9rb2k/tcl9.0.1/pkgs/tdbc1.1.10/library"

# Additional flags that must be passed to the C compiler to use tdbc
tdbc_CFLAGS=
TDBC_CFLAGS=

