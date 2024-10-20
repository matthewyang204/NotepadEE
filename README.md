# Notepad==
Have you ever wanted to jot something down on a Unix system and wished the Windows Notepad were there? Then you can use Notepad== to jot stuff down! Notepad== is a quick and simple text editor for POSIX systems. Additionally, on Windows, this is a better notepad that has more features than the built-in one.

------
macOS
------

System requirements:

Apple Silicon Version: macOS 11.0 or above

Intel Silicon Version: macOSX 10.9 or above

You can download prebuilt universal (works on both apple silicon and intel silicon) binaries in the Releases

Binaries are signed with a personal certificate, meaning they will say unidentified developer if downloaded on a Mac with default security settings (I didn't pay for the official notarization/developer program because it's just extremely expensive, at $99 annually)

Run this in order to get rid of gatekeeper's annoying warnings (gatekeeper is the built-in security thingy) in a new terminal:
```
sudo spctl --master-disable
```
You need to run this under an admin account (log into one) and it requires that account's password

Note: The feature of launching a new instance does not work unless the app bundle is placed in /Applications in the root of your Mac's drive.

macOS build instructions:
- Run `git clone https://github.com/matthewyang204/NotepadEE.git` download the latest source code
- Run `cd NotepadEE/macOS` to enter the macOS build directory
- Let's run `./configure` to find out what you're missing
- Download the missing stuff, ideally with a package manager, and add it to your PATH if needed
- Run `./configure` again
- Repeat if it failed
- If it comes out perfectly, run `make` to build the software from source
- Run `sudo make install` if you don't already have an installation
- If you do already have one, run `sudo make upgrade` to upgrade your installation

-----
Linux
-----
- Download latest dev source code from the Linux repository: https://github.com/matthewyang204/NotepadEE/tree/main/Linux
- These binaries are next to the macOS binaries
- Any GUI distro from the last 10-15 years should work for building from source and running binaries

Linux build instructions:
- Please unzip the folder and then cd into the Linux folder within the extracted folder in a terminal
- Type `./configure && make && sudo make install` to build from source and install
- If the configure script needs to install stuff, enter your password if prompted
- You can use `sudo make upgrade` instead of `sudo make install` to directly update your existing installation
- Requires Debian-based distro to build
- Source code is in the Linux folder; macOS source code is in separate macOS folder

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