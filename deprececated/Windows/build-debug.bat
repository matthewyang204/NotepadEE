@echo off
pyinstaller --hide-console hide-early --hidden-import=tkinter -i Notepad.ico src\Notepad==.py