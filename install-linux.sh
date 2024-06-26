#!/bin/bash

# 1. Check whether the system is AMD64.
if [ "$(uname -m)" != "x86_64" ]; then
    echo "This software is only compatible with AMD64 systems."
    exit 1
fi

# 2. Download the zip file to the Downloads folder and extract it.
echo "Downloading the necessary files..."
cd ~/Downloads
wget https://github.com/matthewyang204/NotepadEE/releases/download/2.2/NotepadEE-Linux.zip

echo "Unpacking Notepad==..."
unzip NotepadEE-Linux.zip
cd Notepad==

# 3. Check whether matthewyang folder exists in /opt. If not, create it.
echo "Creating necessary directories..."
if [ ! -d "/opt/matthewyang" ]; then
    sudo mkdir /opt/matthewyang
fi

# 4. Copy the Notepad== folder from the extracted contents of the zip to /opt/matthewyang/ folder.
echo "Copying necessary files..."
sudo cp -r ./Notepad== /opt/matthewyang/Notepad==

# 5. Symlink /opt/matthewyang/Notepad==/Notepad== to /usr/local/bin/notepadee
sudo ln -s /opt/matthewyang/Notepad==/Notepad== /usr/local/bin/notepadee

# 6. Copy notepadee.desktop from the extracted zip to the /usr/share/applications/ folder
sudo cp notepadee.desktop /usr/share/applications/notepadee.desktop
sudo update-desktop-database

echo "Cleaning up..."
cd ~/Downloads
sudo rm -R NotepadEE-Linux.zip
sudo rm -R Notepad==
sudo rm -R _MACOSX
