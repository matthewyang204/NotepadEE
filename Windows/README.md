# Notepad== Windows Version

This is the repository for the Windows version of this software.

Main repository: https://www.github.com/matthewyang204/NotepadEE

This is the Windows version's source code

The Windows binaries can be downloaded from the releases

Any PC running Windows 7 x64 or later works

Build instructions:
- Run the command prompt as admin and navigate to the cloned repository.
- Run `dpinstall.bat` in the Command Prompt to find out what's missing. Install the missing component that the batch script specifies if it fails.
- If all dependencies are met, it will automatically use pip3 to install the needed Python libraries.
- Once dependencies are met, run `build.bat`.
- Download and install Inno Setup if you haven't already. Then, open the .iss setup script and build by clicking Build>Compile.
- Run the installer and you've successfully installed.

Installing from the precompiled binaries:
- Binaries are next to all other binaries
- x64 binaries are provided for users, however, they are not signed
- Version compatibility:
- Windows 7 x64 or later; ARM64 systems need Win11 ARM64 or later
- Note: The Windows binaries are compiled with a special [build](https://github.com/adang1345/PythonWin7) of Python 3.12 that supports 64-bit Windows 7 - 8.1 alongside 10 and 11.

Upgrading:
- You can directly run the new installer to upgrade. You can either download this from the Release of the new version or you can install from your custom-built installer.
