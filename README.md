# Notepad==
Simple notepad for Macs

System requirements:

Apple Silicon Version: macOS 11.0 or above

Intel Silicon Version: macOSX 10.4 or above

You can download prebuilt universal (works on both apple silicon and intel silicon) binaries in the Releases

Binaries are signed with a personal certificate, meaning they will say unidentified developer if downloaded on a Mac with default security settings

If you're interested, read this: https://www.wikihow.com/Install-Software-from-Unsigned-Developers-on-a-Mac

If you don't want to edit your privacy settings, after downloading the binary, extracting the .zip file, and moving the unzipped app to the Applications folder on your root drive, run this to bypass gatekeeper if it doesn't show a blue open button in the popup:
```
xattr -d com.apple.quarantine /Applications/Notepad==.app
xattr -d com.apple.quarantine /Applications/Notepad==.app/Contents/Resources/Clone/Notepad==.app
```

Note: The feature of launching a new instance does not work unless the app bundle is placed in /Applications in the root of your Mac's drive.

Linux:
- Older x.1.x releases will work on Linux when compiled from source
- Latest x.1.x version is 4.1.x
- Download latest dev source code from the Linux repository: https://github.com/matthewyang204/NotepadEE/tree/main/Linux
- Download latest release source code for Linux, 4.1.2, here: https://github.com/matthewyang204/NotepadEE/releases/tag/4.1.2

Linux build instructions:
- Please unzip the folder and then cd into the Linux folder within the extracted folder in a terminal
- Type `./configure && make && sudo make install` to build from source and install
- Make sure pillow, tkinter, and pyinstaller are installed with pip3, and pip3 is installed with Python before building
