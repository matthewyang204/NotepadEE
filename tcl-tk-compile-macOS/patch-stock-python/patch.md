# Patching stock Python

**1. [0001] Patch Tcl/Tk from 8.6.16 to 8.6.17**
On macOS, the official Python.org packages use Tcl/Tk `8.6.16` instead of `8.6.17`. If compiling with this copy of the library, then the program will complain on launch and exit immediately. This patch fixes that if patched with `-p1` with the current working directory set to the macOS directory.
