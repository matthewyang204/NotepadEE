#!/bin/bash

echo "Setup is checking for and deleting files for previous version to avoid conflicts, enter admin password if asked..."
sudo rm -R /Applications/Notepad==.app '/Applications/Notepad== 3.app'
sudo rm -R ~/Downloads/Notepad==.app ~/Downloads/NotepadEE-Mac.zip

echo "Setup is downloading files..."
cd ~/Downloads
wget https://github.com/matthewyang204/NotepadEE/releases/download/3.1.0/NotepadEE-macOS-x86_64.zip

echo "Setup is unpacking files..."
unzip NotepadEE-macOS-x86_64.zip

echo "Setup is moving files, please enter admin password when asked..."
sudo mv 'Notepad==.app' /Applications/
xattr -d com.apple.quarantine /Applications/Notepad==.app

echo "Setup is cleaning up..."
sudo rm -R NotepadEE-macOS-x86_64.zip
echo "Setup is closing..."#!/bin/bash

echo "Setup is checking for and deleting files for previous version to avoid conflicts, enter admin password if asked..."
sudo rm -R /Applications/Notepad==.app '/Applications/Notepad== 3.app'
sudo rm -R ~/Downloads/Notepad==.app ~/Downloads/NotepadEE-Mac.zip

echo "Setup is downloading files..."
cd ~/Downloads
wget https://github.com/matthewyang204/NotepadEE/releases/download/3.1.0/NotepadEE-macOS-x86_64.zip

echo "Setup is unpacking files..."
unzip NotepadEE-macOS-x86_64.zip

echo "Setup is moving files, please enter admin password when asked..."
sudo mv 'Notepad==.app' /Applications/
xattr -d com.apple.quarantine /Applications/Notepad==.app

echo "Setup is cleaning up..."
sudo rm -R NotepadEE-macOS-x86_64.zip
echo "Setup is closing..."