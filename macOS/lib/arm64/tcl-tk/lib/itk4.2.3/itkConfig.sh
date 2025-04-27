# itkConfig.sh --
#
# This shell script (for sh) is generated automatically by Itk's
# configure script.  It will create shell variables for most of
# the configuration options discovered by the configure script.
# This script is intended to be included by the configure scripts
# for Itk extensions so that they don't have to figure this all
# out for themselves.  This file does not duplicate information
# already provided by tclConfig.sh, tkConfig.sh or itclConfig.sh,
# so you may need to use those files in addition to this one.
#
# The information in this file is specific to a single platform.

# Itcl's version number.
ITCL_VERSION='4.3.2'

# The name of the Itk library (may be either a .a file or a shared library):
ITK_LIB_FILE=libtcl9itk4.2.3.dylib

# String to pass to linker to pick up the Itk library from its
# build directory.
ITK_BUILD_LIB_SPEC='-L/private/tmp/tcl-tk--itk4-20250112-6051-6ccf8k/itk-itk-4-2-3 -litk4.2.3'

# String to pass to linker to pick up the Itk library from its
# installed directory.
ITK_LIB_SPEC='-L/opt/homebrew/Cellar/tcl-tk/9.0.1/lib/itk4.2.3 -litk4.2.3'

# The name of the Itk stub library (a .a file):
ITK_STUB_LIB_FILE=libitkstub4.2.3.a

# String to pass to linker to pick up the Itk stub library from its
# build directory.
ITK_BUILD_STUB_LIB_SPEC='-L/private/tmp/tcl-tk--itk4-20250112-6051-6ccf8k/itk-itk-4-2-3 -litkstub4.2.3'

# String to pass to linker to pick up the Itk stub library from its
# installed directory.
ITK_STUB_LIB_SPEC='-L/opt/homebrew/Cellar/tcl-tk/9.0.1/lib/itk4.2.3 -litkstub4.2.3'

# Location of the top-level source directories from which [incr Tk]
# was built.  This is the directory that contains a README file as well
# as subdirectories such as generic, unix, etc.  If [incr Tk] was
# compiled in a different place than the directory containing the source
# files, this points to the location of the sources, not the location
# where [incr Tk] was compiled.
ITK_SRC_DIR='/private/tmp/tcl-tk--itk4-20250112-6051-6ccf8k/itk-itk-4-2-3'
