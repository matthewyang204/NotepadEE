# Notepad==
Have you ever wanted to jot something down on a Unix system and wished the Windows Notepad were there? Then you can use Notepad==! Notepad== is a quick and simple text editor for POSIX systems.

-----
Linux
-----
- Download latest dev source code from the Linux section of this repository: https://github.com/matthewyang204/NotepadEE/tree/main/Linux
- These binaries are next to the Windows binaries
- Any Debian-based distro should work for building
- Any GUI distro from the last 10-15 years should work for running binaries
- You need Python 3.4 or later

Linux build instructions:
- Please clone the repo and cd into it
- If you haven't yet, please run the `dpinstall` script to install dependencies to your system
- Type `./configure && make && sudo make install` to build from source and install
- If the `./configure` script needs to install stuff, enter your password if prompted
- You can use `sudo make upgrade` instead of `sudo make install` to directly update your existing installation
- Requires Debian-based distro to build
- Source code is in the Linux folder; Windows source code is in separate Windows folder

-----
macOS
-----
Source code located in the [macOS section](https://github.com/matthewyang204/NotepadEE/tree/main/macOS).

Any Mac capable of running Python 3.4 works for building. Therefore, your Mac must be capable of running OS X 10.5 Leopard or later, as it is the earliest version of macOS supported by Python 3.4.

Hackintoshes are supported.

I have separate binaries for Intel and Apple Silicon macs. Please download the correct one. I have signed it with a self-signed signature and can't afford the full Apple Developer notarization. On macOS Sonoma or below, you can bypass the warnings by right-clicking the app and selecting "Open". On macOS Sequioa or later, you will need to disable Gatekeeper entirely by running `sudo spctl --master-disable` and then selecting "Anywhere" at the bottom of the Privacy & Security section of the settings in the "Allow apps from" setting. Alternatively, you may want to use homebrew, which is capable of bypassing Gatekeeper on installation with a single flag.

To use it, first, tap my homebrew repo by running `brew tap matthewyang204/homebrew-formulae-casks`. After this, you can install the cask with `brew install --cask --no-quarantine notepadee`.

All of the prebuilt binaries provided in the Releases support macOS Catalina or newer.

Signing info for prebuilt binaries:
- Self-signed signature
- Name of signature is "Matthew Yang"

Prebuild requirements:
- Python 3.4 - 3.12
- `make` installed
- `gettext` and `tcl-tk` installed with Homebrew

Build instructions:
1. Clone the repository and navigate to the macOS folder inside of it
2. Run `chmod +x autogen.sh` to give the script execute permissions.
3. Run `./autogen.sh --arch=<x86_64 or arm64>` to automatically configure and build. Note that --arch is optional and if you only want to compile for your machine's native architecture, just run `./autogen.sh`.
4. After you're done compiling, you can use `sudo make install` to install.
