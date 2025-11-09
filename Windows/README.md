# Notepad== Windows Version

This is the repository for the Windows version of this software.

Main repository: https://www.github.com/matthewyang204/NotepadEE

This is the Windows version's source code

The Windows binaries can be downloaded from the releases

Any PC running Windows 7/10 or later works depending on what installer you use

Requirements:
- Windows 10 x64 or later
- Additional requirements may be needed for building from source:
    - Windows 7 or later is supported for building from source, but Windows 10 or later is recommended
    - Python 3.6 or later
    - Inno Setup

Build instructions:
- Please clone the repo and cd into the Windows folder
- `./configure` - configure the stuff
- `make -j<number of CPU cores>` - build with pyinstaller
- `make bin-dist` - create installer with Inno Setup

Installing from the precompiled binaries:
- Windows installers (.exe) are available in the Releases section of this repository
- Simply download the installer and run it
- Support:
    - Windows 10 or later for official installers
    - Windows 7 and 8 may work but only with custom-built installers - official installers are not built for these versions due to small Python incompatibilities

Upgrading:
- You can directly run the new installer to upgrade