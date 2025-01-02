# Notepad== macOS Version
This is the repository for the macOS version of this software.

Main repository: https://www.github.com/matthewyang204/NotepadEE

Any Mac capable of running Python 3.4 or later works for building. Therefore, your Mac must be capable of running macOSX 10.9 Mavericks or later in order to build, as it is the earliest version of macOSX capable of running Python 3.4.

Hackintoshes are supported.

I have separate binaries for Intel and Apple Silicon macs. Please download the correct one. I have signed it with a self-signed signature and can't afford the full Apple Developer notarization. On macOS Sonoma or below, you can bypass the warnings by right-clicking the app and selecting "Open". On macOS Sequioa or later, you will need to disable Gatekeeper entirely by running `sudo spctl --master-disable` and then selecting "Anywhere" at the bottom of the Privacy & Security section of the settings in the "Allow apps from" setting.

# Prebuild requirements
- Python 3.4 to 3.12
- make installed
- `configure` script will automatically install Python packages

# Build instructions
1. Clone the repository and navigate to the macOS folder inside of it
2. Run `./autogen.sh --arch=<x86_64 or arm64>` to automatically configure and build
5. After you're done compiling, you can use `sudo make install` to install.
