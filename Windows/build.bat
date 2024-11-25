@echo off
pyinstaller --noconsole --hidden-import=tkinter -i Notepad.ico src\Notepad==.py