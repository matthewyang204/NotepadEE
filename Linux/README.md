# Notepad== Linux Version

This is the repository for the linux version of this software.

Main repository: https://www.github.com/matthewyang204/NotepadEE

This is the Linux version's source code

The Linux binaries can be downloaded from the releases

Any Debian-based distro works for building, otherwise, any distro can be used with the binaries

Build instructions:
- Please unzip the folder and then cd into the Linux folder within the extracted folder in a terminal
- Type `sudo ./configure && make && sudo make install` to build from source and install
- You can use `sudo make upgrade` instead of `sudo make install` to directly update your existing installation
- Debian-based distro is required to build
- `sudo` is required because my `./configure` script automatically installs dependencies with `apt` and `pip3`.
