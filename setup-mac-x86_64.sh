#!/bin/bash

echo "Setup is checking for and deleting files for previous version to avoid conflicts, enter admin password if asked..."
sudo rm -R /Applications/Notepad==.app
sudo rm -R ~/Downloads/Notepad==.app ~/Downloads/NotepadEE-Mac.zip

echo "Setup is downloading files..."
cd ~/Downloads
wget https://github.com/matthewyang204/NotepadEE/releases/download/3.0.0/NotepadEE-3-x86_64-macOS.zip

echo "Setup is unpacking files..."
unzip NotepadEE-3-x86_64-macOS.zip

echo "Setup is moving files, please enter admin password when asked..."
sudo mv 'Notepad== 3.app' /Applications/

echo "Setup is cleaning up..."
sudo rm -R NotepadEE-Mac.zip
echo "Setup is closing..."