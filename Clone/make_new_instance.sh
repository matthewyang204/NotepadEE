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

NUM=0
for (( NUM=0; ; NUM++ )); do
  if [ ! -e "${TARGET_DIR}/Notepad==$NUM$EXT" ]; then
    break
  fi
done

cp -R "${TARGET_DIR}/Notepad==0${EXT}" "${TARGET_DIR}/Notepad==$NUM$EXT"

open -a "${TARGET_DIR}/Notepad==$NUM$EXT"