# Notepad==
Simple notepad for POSIX systems

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

-----
Linux
-----
- Download latest dev source code from the Linux repository: https://github.com/matthewyang204/NotepadEE/tree/main/Linux
- These binaries are next to the macOS binaries
- Any debian-based distro from the last 10-15 years should work for building, binaries work with just about any GUI distro

Linux build instructions:
- Please unzip the folder and then cd into the Linux folder within the extracted folder in a terminal
- Type `sudo ./configure && make && sudo make install` to build from source and install
- You can use `sudo make upgrade` instead of `sudo make install` to directly update your existing installation
- Requires Debian-based distro to build
- `sudo` is required because my `./configure` script installs dependencies automatically with `apt` and `pip3`.
- Source code is in the Linux folder; macOS source code is in separate macOS folder
