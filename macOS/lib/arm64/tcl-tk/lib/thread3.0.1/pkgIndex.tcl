# -*- tcl -*-
# Tcl package index file, version 1.1
#

# Tcl 8.7 interps are only supported on 32-bit platforms.
# Lower than that is never supported. Bye!
if {![package vsatisfies [package provide Tcl] 9.0]
	&& ((![package vsatisfies [package provide Tcl] 8.7])
	|| ($::tcl_platform(pointerSize)!=4))} {
    return
}

# All Tcl 8.7+ interps can [load] thread 3.0.1
#
# For interps that are not thread-enabled, we still call [package ifneeded].
# This is contrary to the usual convention, but is a good idea because we
# cannot imagine any other version of thread that might succeed in a
# thread-disabled interp.  There's nothing to gain by yielding to other
# competing callers of [package ifneeded Thread].  On the other hand,
# deferring the error has the advantage that a script calling
# [package require Thread] in a thread-disabled interp gets an error message
# about a thread-disabled interp, instead of the message
# "can't find package thread".

package ifneeded [string tolower thread] 3.0.1 \
    [list load [file join $dir libtcl9thread3.0.1.dylib] [string totitle thread]]
package ifneeded [string totitle thread] 3.0.1 \
    [list package require -exact [string tolower thread] 3.0.1]

# package ttrace uses some support machinery.

# In Tcl 8.7+ interps; use [::apply]

package ifneeded ttrace 3.0.1 [list ::apply {{dir} {
    if {[info exists ::env(TCL_THREAD_LIBRARY)] &&
	[file readable $::env(TCL_THREAD_LIBRARY)/ttrace.tcl]} {
	source $::env(TCL_THREAD_LIBRARY)/ttrace.tcl
    } elseif {[file readable [file join $dir .. lib ttrace.tcl]]} {
	source [file join $dir .. lib ttrace.tcl]
    } elseif {[file readable [file join $dir ttrace.tcl]]} {
	source [file join $dir ttrace.tcl]
    } elseif {[file exists //zipfs:/lib/thread/ttrace.tcl] ||
              ![catch {zipfs mount [file join $dir libtcl9thread3.0.1.dylib] //zipfs:/lib/thread}]} {
	source //zipfs:/lib/thread/ttrace.tcl
    }
    if {[namespace which ::ttrace::update] ne ""} {
	::ttrace::update
    }
}} $dir]
package ifneeded Ttrace 3.0.1 \
    [list package require -exact ttrace 3.0.1]




