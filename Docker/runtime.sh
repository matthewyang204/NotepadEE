#!/bin/bash

apt-get update
apt install git x11-apps sudo
cd /home
git clone https://www.github.com/matthewyang204/NotepadEE.git
cd NotepadEE/Linux
./configure
make
sudo make install
cd /home
rm -rf NotepadEE
notepadee