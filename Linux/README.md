# Notepad== Linux Version

This is the repository for the linux version of this software.

Main repository: https://www.github.com/matthewyang204/NotepadEE

This is the Linux version's source code

The Linux binaries can be downloaded from the releases

Any Debian-based distro works for building, otherwise, any distro can be used with the binaries

Python 3.12 is required for building due to syntax reasons.

Build instructions:
- Please clone the repo and then cd into the Linux folder within the cloned repo in a terminal
- If you haven't yet, please run the `dpinstall` script to install dependencies if you haven't yet
- Type `./configure && make && sudo make install` to build from source and install
- If the `./configure` script needs to install stuff, go ahead and enter your password if prompted
- You can use `sudo make upgrade` instead of `sudo make install` to directly update your existing installation
- Any GUI distro from the last 10-15 years should work for building from source and running binaries
- Source code is in the Linux folder; macOS source code is in separate macOS folder
