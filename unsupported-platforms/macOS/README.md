------
macOS version (not supported anymore as of 10/24/2024)
------

Note: macOS version is not supported anymore, will not plan to update in the forseeable future. Last update was v4.3.1.

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