@echo off
pyinstaller --noconsole --hidden-import=tkinter -i src\Notepad.ico src\Notepad==.py
copy Notepad.ico "dist\Notepad==\"