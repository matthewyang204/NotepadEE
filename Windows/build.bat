nuitka --standalone --enable-plugin=tk-inter --output-dir=dist src/Notepad==.py
copy Notepad.png dist/Notepad==/
echo "Build completed. To install, compile the Inno Setup installer and then run it."