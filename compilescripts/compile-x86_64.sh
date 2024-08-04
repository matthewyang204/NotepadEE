#!/bin/bash

echo "Compiling Notepad=="
echo "Compiling main first..."
/usr/local/homebrew/bin/pyinstaller --windowed -i Notepad.png --hidden-import=tkinter Notepad==.py
echo "done

echo "Caching compiled main..."
mv dist/Notepad==.app ~/Downloads/
rm -rf dist/*
echo "done"

echo "Now compiling clone..."
/usr/local/homebrew/bin/pyinstaller --windowed -i Notepad.png --hidden-import=tkinter Clone/Notepad==.py
echo "done"

echo "Assembling binary..."
mkdir ~/Downloads/Notepad==.app/Contents/Resources/Clone
mv dist/* ~/Downloads/Notepad==.app/Contents/Resources/Clone/
echo "done"

echo "Packaging app..."
cd ~/Downloads
7z a -tzip Notepad==.zip Notepad==.app
echo "done"
