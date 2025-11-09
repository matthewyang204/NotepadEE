# Notepad==
Have you ever wanted to jot something down on a Unix system and wished the Windows Notepad were there? Then you can use Notepad==! Notepad== is a quick and simple text editor for POSIX systems.


# Linux
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

# macOS
Source code located in the [macOS section](https://github.com/matthewyang204/NotepadEE/tree/main/macOS).

Any Mac capable of running Python 3.4 works for building. Your Mac must be capable of running OS X 10.4 Tiger or later. OS X 10.5 Leopard is the earliest version of OS X supported by Python 3.4, so it is the earliest officially supported version. However, Tiger is also fine because it can actually run a very modern version of Python (3.10.16) via [Tigerbrew](https://github.com/mistydemeo/Tigerbrew).

Hackintoshes are supported.

I have separate binaries for Intel and Apple Silicon macs. Please download the correct one. I have signed it with a self-signed signature and can't afford the full Apple Developer notarization. On macOS Sonoma or below, you can bypass the warnings by right-clicking the app and selecting "Open". On macOS Sequioa or later, you will need to disable Gatekeeper entirely by running `sudo spctl --master-disable` and then selecting "Anywhere" at the bottom of the Privacy & Security section of the settings in the "Allow apps from" setting. Alternatively, you may want to use homebrew, which is capable of bypassing Gatekeeper on installation with a single flag.

To use it, first, tap my homebrew repo by running `brew tap matthewyang204/homebrew-formulae-casks`. After this, you can install the cask with `brew install --cask --no-quarantine notepadee`. Also, installing with Homebrew will add a convenient `notepadee` command that launches the app from the terminal. Simply run `notepadee` for a new blank editor, or run `notepadee <yourfile>` to open a file.

All of the prebuilt binaries provided in the Releases support macOS Catalina or newer.

Signing info for prebuilt binaries:
- Self-signed signature
- Name of signature is "Matthew Yang"

Prebuild requirements:
- Python 3.4 - 3.13 in PATH, built with tkinter support
- `make` installed
- `gettext` and `tcl-tk@8` installed

Build instructions:
1. Clone the repository and navigate to the macOS folder inside of it
2. Run `chmod +x autogen.sh` to give the script execute permissions.
3. Run `./autogen.sh --arch=<x86_64 or arm64>` to automatically configure and build. Note that `--arch` is optional and if you only want to compile for your machine's native architecture, just run `./autogen.sh`. You can also use `--gettext=<yourgettext>` to specify a gettext install root dir and `--tcl-tk=<yourtcltk>` to specify custom tcl-tk install root dir, assuming both `tcl` and `tk` are installed in the same prefix. They *must* be installed in the same prefix.
4. After you're done compiling, you can use `sudo make install` to install.

# Windows
Source code located in the [Windows section](Windows/)

Any PC running Windows 7/10 or later works depending on what installer you use

## Requirements
- Windows 10 x64 or later
- Additional requirements may be needed for building from source:
    - Windows 7 or later is supported for building from source, but Windows 10 or later is recommended
    - Python 3.6 or later
    - Inno Setup

## Build instructions
- Please clone the repo and cd into the Windows folder
- `./configure` - configure the stuff
- `make -j<number of CPU cores>` - build with pyinstaller
- `make bin-dist` - create installer with Inno Setup

## Installation
Installing from the precompiled binaries:
- Windows installers (.exe) are available in the Releases section of this repository
- Simply download the installer and run it
- Support:
    - Windows 10 or later for official installers
    - Windows 7 and 8 may work but only with custom-built installers - official installers are not built for these versions due to small Python incompatibilities

Upgrading:
- You can directly run the new installer to upgrade

-------
License
-------
This project is licensed under the GNU General Public License v3.0 (GPLv3).  
All past and future versions of Notepad== are covered by this license.  
See the LICENSE file for full details.
