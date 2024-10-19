xcopy /E /I "dist\Notepad==.dist" "dist\Notepad=="
rcedit dist\Notepad==\Notepad==.exe --set-icon Notepad.ico
echo "Build completed. To install, compile the Inno Setup installer and then run it."