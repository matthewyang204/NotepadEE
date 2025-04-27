if {![package vsatisfies [package provide Tcl] 8.7-]} return
if {[package vsatisfies [package provide Tcl] 9.0]} {
    package ifneeded tk 9.0.1 [list load [file normalize [file join $dir .. libtcl9tk9.0.dylib]]]
} else {
    package ifneeded tk 9.0.1 [list load [file normalize [file join $dir .. libtk9.0.dylib]]]
}
package ifneeded Tk 9.0.1 [list package require -exact tk 9.0.1]
