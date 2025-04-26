# -*- tcl -*-
# Tcl package index file, version 1.1
#
if {[package vsatisfies [package provide Tcl] 9.0-]} {
    package ifneeded tls 1.8.0 [list apply {{dir} {
	# Load library
	load [file join $dir libtcl9tls1.8.0.dylib] [string totitle tls]

	# Source init file
	set initScript [file join $dir tls.tcl]
	if {[file exists $initScript]} {
	    source -encoding utf-8 $initScript
	}
    }} $dir]
} else {
    if {![package vsatisfies [package provide Tcl] 8.5]} {return}
    package ifneeded tls 1.8.0 [list apply {{dir} {
	# Load library
	if {[string tolower [file extension libtls1.8.0.dylib]] in [list .dll .dylib .so]} {
	    # Load dynamic library
	    load [file join $dir libtls1.8.0.dylib] [string totitle tls]
	} else {
	    # Static library
	    load {} [string totitle tls]
	}

	# Source init file
	set initScript [file join $dir tls.tcl]
	if {[file exists $initScript]} {
	    source -encoding utf-8 $initScript
	}
    }} $dir]
}
