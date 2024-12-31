@echo off
python -m pyinstaller --noconsole --hidden-import=tkinter -i Notepad.ico src\Notepad==.py