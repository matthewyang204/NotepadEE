import tkinter as tk
from tkinter import filedialog
import os
from tkinter import messagebox
import subprocess
import shutil
import sys
from Cocoa import NSObject, NSApplication, NSEvent, NSAppleEventManager, NSURL
from PyObjCTools import AppHelper
import threading

global file_open
global current_file
file_open=0
last_file_path  = os.path.join(os.path.expanduser('~'),  'Library', 'Caches', 'NotepadEE', 'last_file_path')
if os.path.exists(last_file_path):
    with open(last_file_path, 'r') as file:
        current_file  = file.read()
        if current_file.strip() == '':  
            file_open = 0
        else:
            file_open = 1
    
else:
    current_file  =  ""
    file_open=0

last_write=os.path.join(os.path.expanduser('~'),  'Library', 'Caches', 'NotepadEE', 'last_write')
folder_path  = os.path.join(os.path.expanduser('~'),  'Library', 'Caches', 'NotepadEE')
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

make_new_instance = """#!/bin/bash

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
"""

instanceshellscriptpath = os.path.join(os.path.expanduser('~'), 'Library', 'Caches', 'NotepadEE', 'make_new_instance.sh')

with open(instanceshellscriptpath, "w") as f:
    f.write(make_new_instance)

def write_cache(event=None):
    global current_file
    global file_open
    with open(os.path.join(os.path.expanduser('~'), 'Library', 'Caches', 'NotepadEE', 'last_write'), 'w') as file:
        file.write(text_area.get('1.0', 'end-1c'))
    last_file_path = os.path.join(os.path.expanduser('~'), 'Library', 'Caches', 'NotepadEE', 'last_file_path')
    with open(last_file_path, 'w') as file:
        file.write(current_file)
    if file_open==1:
        try:
            with open(current_file, 'w') as file:
                text = text_area.get('1.0', 'end-1c')
                file.write(text)
        except FileNotFoundError:
            file_open = 0
    root.after(5000, write_cache)

def save_as(event=None):
    global current_file
    global file_open
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    current_file=file_path
    with open(file_path, 'w') as file:
        text = text_area.get(1.0, "end-1c")
        file.write(text)
    write_cache()
    file_open=1

def save_file(event=None):
    global current_file
    global file_open
    if file_open==1:
        with open(current_file, 'w') as file:
            text = text_area.get('1.0', 'end-1c')
            file.write(text)
        write_cache()
    else:
        response = messagebox.askyesno("Create new file", "The file does not exist. Do you want to create it as a new file?")
        if response:
            save_as()

def clear(event=None):
    global current_file, file_open
    global current_file
    global file_open
    if current_file != "":
        with open(current_file, 'w') as file:
            text = text_area.get('1.0', 'end-1c')
            file.write(text)
    text_area.delete(1.0, "end")
    current_file=""
    write_cache()
    file_open=0

def open_file(event=None):
    global current_file, file_open
    file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    if file_path:
        clear()
        text_area.delete(1.0, "end")
        current_file=file_path
        with open(file_path, 'r') as file:
            text_area.insert(1.0, file.read())
    file_open=1

def open_file_arg(macOS_file_path=None):
    file_path=macOS_file_path
    global current_file, file_open
    if file_path:
        text_area.delete(1.0, "end")
        current_file=file_path
        with open(file_path, 'r') as file:
            text_area.insert(1.0, file.read())
    write_cache()
    file_open=1

file_to_open = None

class AppDelegate(NSObject):
    def application_openFile_(self, app, file_url):
        # This method is called when a file is opened with your application
        global file_to_open
        file_to_open = file_url.path()  # Store the file path in the global variable
        return True

def macOS_file_open():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    app.setDelegate_(delegate)
    # Initialize functions, variables, and the GUI here
    # ...
    # Then, if a file was opened with the application, open it in the text editor
    if file_to_open is not None:
        open_file_arg(file_to_open)

def cut_text(event=None):
    text_area.clipboard_clear()
    text_area.clipboard_append(text_area.get("sel.first", "sel.last"))
    text_area.delete("sel.first", "sel.last")
    return 'break'

def copy_text(event=None):
    text_area.clipboard_clear()
    text_area.clipboard_append(text_area.get("sel.first", "sel.last"))
    return 'break'

def paste_text(event=None):
    text_area.insert("insert", text_area.clipboard_get())
    return 'break'

def select_all_text(event=None):
    text_area.tag_add("sel", "1.0", "end")
    return 'break'

def add_instance(event=None):
  subprocess.run(["/bin/bash", instanceshellscriptpath])

def clear_instances(event=None):
    response2 = messagebox.askyesno("Clear instances", "Are you sure you want to clear all instances? Make sure to close all other instances before clearing. Click 'No' to get back to clear all other instances.")
    if response2:
        folder_path = os.path.join(os.path.expanduser('~'), 'Library', 'Caches', 'NotepadEE', 'Instances')
        shutil.rmtree(folder_path)

root = tk.Tk()
ask_quit = False
root.title("Notepad==")

text_area = tk.Text(root, width=100, height=80, wrap=tk.WORD)
text_area.pack()
if os.path.exists(last_write):
    text_area.delete(1.0, "end")
    with open(last_write, 'r') as file:
        text_area.insert(1.0, file.read())

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=clear)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save as...", command=save_as)

edit_menu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_command(label="Select All", command=select_all_text)

window_menu = tk.Menu(menu)
menu.add_cascade(label="Window", menu=window_menu)
window_menu.add_command(label="Launch new instance", command=add_instance)
window_menu.add_command(label="Clear all instances", command=clear_instances)

root.bind('<Command-n>', clear)
root.bind('<Command-o>', open_file)
root.bind('<Command-s>', save_file)
root.bind('<Command-S>', save_as)

text_area.bind('<Command-x>', cut_text)
text_area.bind('<Command-c>', copy_text)
text_area.bind('<Command-v>', paste_text)
text_area.bind('<Command-a>', select_all_text)

root.bind('<Command-l>', add_instance)
root.bind('<Command-L>', clear_instances)

write_cache()
threading.Thread(target=macOS_file_open).start()
root.mainloop()
