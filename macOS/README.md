# Notepad== macOS Version
This is the repository for the macOS version of this software.

Main repository: https://www.github.com/matthewyang204/NotepadEE

Any Mac capable of running Python 3.4 works for building. Your Mac must be capable of running OS X 10.4 Tiger or later. OS X 10.5 Leopard is the earliest version of OS X supported by Python 3.4, so it is the earliest officially supported version. However, Tiger is also fine because it can actually run a very modern version of Python (3.10.16) via [Tigerbrew](https://github.com/mistydemeo/Tigerbrew).

Hackintoshes are supported.

I have separate binaries for Intel and Apple Silicon macs. Please download the correct one. I have signed it with a self-signed signature and can't afford the full Apple Developer notarization. On macOS Sonoma or below, you can bypass the warnings by right-clicking the app and selecting "Open". On macOS Sequioa or later, you will need to disable Gatekeeper entirely by running `sudo spctl --master-disable` and then selecting "Anywhere" at the bottom of the Privacy & Security section of the settings in the "Allow apps from" setting. Alternatively, you may want to use homebrew. 

To use it, first, tap my homebrew repo by running `brew tap matthewyang204/homebrew-formulae-casks`. After this, you can install the cask with `brew install --cask --no-quarantine notepadee`.

All of the prebuilt binaries provided in the README support macOS Catalina or newer.

# Signing info for prebuilt binaries:
- Self-signed signature
- Name of signature is "Matthew Yang"

# Prebuild requirements
- Python 3.4 - 3.13 in PATH, built with tcl-tk
- make installed
- `configure` script will automatically install Python packages
- `gettext` and `tcl-tk@8` installed

# Build instructions
1. Clone the repository and navigate to the macOS folder inside of it
2. Run `chmod +x autogen.sh` to give the script execute permissions.
3. Run `./autogen.sh --arch=<x86_64 or arm64>` to automatically configure and build. Note that --arch is optional and if you only want to compile for your machine's native architecture, just run `./autogen.sh`. You can also use `--gettext=<yourgettext>` to specify a gettext install root dir and `--tcl-tk=<yourtcltk>` to specify custom tcl-tk install root dir, assuming both are installed in the same prefix. They *must* be installed in the same prefix.
4. After you're done compiling, you can use `sudo make install` to install.
