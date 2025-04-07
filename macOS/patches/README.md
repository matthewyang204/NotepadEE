# Notepad== macOS Version
This is the repository for the macOS version of this software.

Main repository: https://www.github.com/matthewyang204/NotepadEE

Any Mac capable of running Python 3.12 works for building. Therefore, your Mac must be capable of running macOSX 10.9 Mavericks or later in order to build, as it is the earliest version of macOS capable of running Python 3.12.

Hackintoshes are supported.

I have separate binaries for Intel and Apple Silicon macs. Please download the correct one. I have signed it with a self-signed signature and can't afford the full Apple Developer notarization. On macOS Sonoma or below, you can bypass the warnings by right-clicking the app and selecting "Open". On macOS Sequioa or later, you will need to disable Gatekeeper entirely by running `sudo spctl --master-disable` and then selecting "Anywhere" at the bottom of the Privacy & Security section of the settings in the "Allow apps from" setting. Alternatively, you may want to use homebrew. 

To use it, first, tap my homebrew repo by running `brew tap matthewyang204/homebrew-formulae-casks`. After this, you can install the cask. On an Intel Mac, you need to install the x86_64 version. Run `brew install --cask --no-quarantine notepadee-x86_64`. On an Apple Silicon Mac, you need to install the arm64 version, so run `brew install --cask --no-quarantine notepadee-arm64`. You can update the cask by running `brew update && brew upgrade notepadee-x86_64` on an Intel Mac or `brew update && brew upgrade notepadee-arm64` on an Apple Silicon Mac.

All of the prebuilt binaries provided in the README support macOS Sierra or newer.

# Signing info for prebuilt binaries:
- Self-signed signature
- Name of signature is "Matthew Yang"

# Prebuild requirements
- Python 3.12
- make installed
- `configure` script will automatically install Python packages

# Build instructions
1. Clone the repository and navigate to the macOS folder inside of it
2. Run `chmod +x autogen.sh` to give the script execute permissions.
3. Run `./autogen.sh --arch=<x86_64 or arm64>` to automatically configure and build. Note that --arch is optional and if you only want to compile for your machine's native architecture, just run `./autogen.sh`.
4. After you're done compiling, you can use `sudo make install` to install.
