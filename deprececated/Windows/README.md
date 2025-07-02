# Notepad== Windows Version

**The Windows version is no longer supported as of Release v5.2.0. This is because being primarily a UNIX developer, I don't even have Windows systems. To do any testing or work on it, I have to use Wine, which screws up hours of my time. Additionally, I'm accustomed to using UNIX-only features and paths, which make the primary Linux codebase incredibly incompatible with Windows.**

This is the repository for the Windows version of this software.

Main repository: https://www.github.com/matthewyang204/NotepadEE

This is the Windows version's source code

The Windows binaries can be downloaded from the releases

Any PC running Windows XP or later works

Build instructions:
- Run the command prompt as admin and navigate to the cloned repository.
- Run `dpinstall.bat` in the Command Prompt to find out what's missing. Install the missing component that the batch script specifies if it fails.
- If all dependencies are met, it will automatically use pip3 to install the needed Python libraries.
- Once dependencies are met, run `build.bat`.
- Download and install Inno Setup if you haven't already. Then, open the .iss setup script and build by clicking Build>Compile. Note that you need to use Inno Setup 5 on Windows Vista or earlier.
- Run the installer and you've successfully installed.

Python 3.4 compatibility scripts:
- There are scripts with `-3.4` appended to their filenames that are compatible with Python 3.4

Installing from the precompiled binaries:
- Binaries are next to all other binaries
- x64 binaries are provided for users, however, they are not signed
- Version compatibility:
- Windows XP or later; ARM64 systems need Win10 ARM64 or later
- Python 3.4 or later

Upgrading:
- You can directly run the new installer to upgrade. You can either download this from the Release of the new version or you can install from your custom-built installer.
