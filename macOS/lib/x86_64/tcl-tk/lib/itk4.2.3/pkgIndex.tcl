# -*- tcl -*-
# Tcl package index file, version 1.1
#

if {![package vsatisfies [package provide Tcl] 8.6-]} {return}
if {[string length [package provide Itcl]] && ![package vsatisfies [package provide Itcl] 4.1]} return
if {[package vsatisfies [package provide Tcl] 9.0-]} {
    package ifneeded itk 4.2.3 \
	    [list load [file join $dir libtcl9itk4.2.3.dylib] Itk]
} else {
    package ifneeded itk 4.2.3 \
	    [list load [file join $dir libitk4.2.3.dylib] Itk]
}

package ifneeded Itk 4.2.3 [list package require -exact itk 4.2.3]
