# Notepad==
Simple notepad for computers without simple-enough notepad software

Main repository: https://www.github.com/matthewyang204/NotepadEE

This is the Linux version's source code

Linux releases will always be in the main repository, numbered x.1.x in the main repository's releases

4.1.0 is the latest x.1.x version

Just about any GUI Linux version released in the last 20-25 years should work

Build instructions:
- Please unzip the folder and then cd into the folder in a terminal
- Type `pyinstaller --hidden-import=tkinter -i Notepad.png Notepad==.py` to compile
- Make sure pillow, tkinter, and pyinstaller are installed with pip3, and pip3 is installed with Python before building
