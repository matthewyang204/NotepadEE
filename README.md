# Notepad==
Have you ever wanted to jot something down on a Unix system and wished the Windows Notepad were there? Or have you ever wanted autosave and line numbering on your Windows 10 system? Then you can use Notepad==! Notepad== is a quick and simple text editor for POSIX systems. On Windows, this is a better notepad that has more features than the built-in one. Notepad== has autosave and line numbering, making it easier to take notes. Additionally, it doesn't carry Microsoft's heavy AI and UWP bloat.

-----
Linux
-----
- Download latest dev source code from the Linux repository: https://github.com/matthewyang204/NotepadEE/tree/main/Linux
- These binaries are next to the Windows binaries
- Any Debian-based distro should work for building
- Any GUI distro from the last 10-15 years should work for running binaries

Linux build instructions:
- Please clone the repo and cd into it
- If you haven't yet, please run the `dpinstall` script to install dependencies to your system
- Type `./configure && make && sudo make install` to build from source and install
- If the configure script needs to install stuff, enter your password if prompted
- You can use `sudo make upgrade` instead of `sudo make install` to directly update your existing installation
- Requires Debian-based distro to build
- Source code is in the Linux folder; Windows source code is in separate Windows folder

-----
Windows
-----
- Download the latest dev source code from the Windows repository: https://github.com/matthewyang204/NotepadEE/tree/main/Windows
- Binaries are next to all other binaries
- x64 binaries are provided for users, however, they are not signed
- Version compatibility:
- Windows 7 x64 or later
- Windows 11 ARM64 or later

Upgrading:
- You can directly run the new installer to upgrade. You can either download this from the Release of the new version or you can install from your custom-built installer.

-----
macOS
-----
Source code located in the [macOS section](https://github.com/matthewyang204/NotepadEE/tree/main/macOS).

Any Mac capable of running Python 3.4 or later works for building. Therefore, your Mac must be capable of running macOSX 10.9 Mavericks or later in order to build, as it is the earliest version of macOSX capable of running Python 3.4.

Binaries are not provided.

Prebuild requirements:
- Python 3.4 or later
- make installed
- `configure` script will automatically install Python packages

Build instructions:
1. Clone the repository and navigate to the macOS folder inside of it
2. Run `sh autogen.sh` to automatically configure and build
