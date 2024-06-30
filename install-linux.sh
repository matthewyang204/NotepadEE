#!/bin/bash

echo "Checking for and deleting any pieces of old installation..."
sudo rm -R /opt/matthewyang/Notepad==
sudo rm -R /usr/share/applications/notepadee.desktop
sudo rm -R /usr/local/bin/notepadee
sudo rm -R ~/Library
cd ~/Downloads
sudo rm -R NotepadEE-3-Linux-AMD64.zip
sudo rm -R Notepad==
sudo rm -R __MACOSX

# 1. Check whether the system is AMD64.
if [ "$(uname -m)" != "x86_64" ]; then
    echo "This software is only compatible with AMD64 systems."
    exit 1
fi

# 2. Download the zip file to the Downloads folder and extract it.
echo "Downloading the necessary files..."
cd ~/Downloads
wget https://github.com/matthewyang204/NotepadEE/releases/download/3.0.0/NotepadEE-3-Linux-AMD64.zip

echo "Unpacking Notepad==..."
unzip NotepadEE-3-Linux-AMD64.zip
cd Notepad==

# 3. Check whether matthewyang folder exists in /opt. If not, create it.
echo "Creating necessary directories..."
if [ ! -d "/opt/matthewyang" ]; then
    sudo mkdir /opt/matthewyang
fi
if [ ! -d "~/Library/Caches/NotepadEE" ]; then
    mkdir ~/Library
    mkdir ~/Library/Caches
    mkdir ~/Library/Caches/NotepadEE
fi    

# 4. Copy the Notepad== folder from the extracted contents of the zip to /opt/matthewyang/ folder.
echo "Copying necessary files..."
sudo cp -r ./Notepad== /opt/matthewyang/Notepad==

# 5. Symlink /opt/matthewyang/Notepad==/Notepad== to /usr/local/bin/notepadee
sudo ln -s /opt/matthewyang/Notepad==/Notepad== /usr/local/bin/notepadee

# 6. Copy notepadee.desktop from the extracted zip to the /usr/share/applications/ folder
sudo cp notepadee.desktop /usr/share/applications/notepadee.desktop
sudo update-desktop-database
sudo chown -R $USER /opt/matthewyang

echo "Cleaning up..."
cd ~/Downloads
sudo rm -R NotepadEE-3-Linux-AMD64.zip
sudo rm -R Notepad==
sudo rm -R __MACOSX
