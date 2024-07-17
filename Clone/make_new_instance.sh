#!/bin/bash

INSTANCES=~/Library/Caches/NotepadEE/Instances
if [ ! -d "$INSTANCES" ]; then
  mkdir "$INSTANCES"
fi

SRC_DIR=/Applications/Notepad==.app/Contents/Resources/Clone
SRC_FILE="Notepad=="

TARGET_DIR=~/Library/Caches/NotepadEE/Instances

EXT=.app

cp -R "$SRC_DIR/Notepad==.app" "${TARGET_DIR}/Notepad==0$EXT"

NUM=1
while [ -f "${TARGET_DIR}/Notepad==$NUM$EXT" ]; do
  ((NUM++))
done

mv "${TARGET_DIR}/Notepad==0${EXT}" "${TARGET_DIR}/Notepad==$NUM$EXT"
open -a "${TARGET_DIR}/Notepad==$NUM$EXT"