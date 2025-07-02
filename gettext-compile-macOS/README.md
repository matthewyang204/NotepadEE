# Compiling gettext for macOS
The contents of this folder allow you to either install a prebuilt copy of gettext or build one yourself to install on your system with macOS High Sierra compatibility, as Homebrew's bottles are built for macOS Sonoma. The precompiled.zip contains an opt folder; drag the contents of the opt folder into your /opt folder to use. Otherwise, you can build one yourself from the tarball directly downloaded from gnu's site. Please follow the build notes.

The patched.mak file is a prepatched file that has been patched to use /opt/gettext instead of homebrew's gettext.

Please resolve all deps yourself.