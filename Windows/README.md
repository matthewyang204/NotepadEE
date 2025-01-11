# Notepad== Windows Version

This is the repository for the Windows version of this software.

Main repository: https://www.github.com/matthewyang204/NotepadEE

This is the Windows version's source code

The Windows binaries can be downloaded from the releases

Any PC running Windows 10 x64 or later works for building, otherwise, Windows 7 x64 or later can be used with the binaries

Build instructions:
- Run the command prompt as admin and navigate to the cloned repository.
- Run `dpinstall.bat` in the Command Prompt to find out what's missing. Install the missing component that the batch script specifies if it fails.
- If all dependencies are met, it will automatically use pip3 to install the needed Python libraries.
- Once dependencies are met, run `build.bat`.
- Download and install Inno Setup if you haven't already. Then, open the .iss setup script and build by clicking Build>Compile.
- Run the installer and you've successfully installed.

Installing from the precompiled binaries:
- Binaries are next to all other binaries
- x64 & x86 binaries are provided for users, however, they are not signed
- Version compatibility:
- x86 version - Windows XP or later
- x64 version - Windows 10 x64 or later; ARM64 systems need Win11 ARM64 or later
- Note: 64-bit Windows 7 - 8.1 systems must build the 64-bit version from source using Python 3.8, as Python 3.13, which the binaries are built with, doesn't support anything older than Windows 10.

Upgrading:
- You can directly run the new installer to upgrade. You can either download this from the Release of the new version or you can install from your custom-built installer.
