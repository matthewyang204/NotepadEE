import tkinter as tk
from tkinter import filedialog
import os
from tkinter import messagebox
import subprocess
import shutil
from tkinter import font

global file_open
global current_file
file_open=0
last_file_path  = os.path.join(os.path.expanduser('~'),  'Library', 'Preferences', 'com.matthewyang.NotepadEE', 'last_file_path')
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

last_write=os.path.join(os.path.expanduser('~'),  'Library', 'Preferences', 'com.matthewyang.NotepadEE', 'last_write')
folder_path  = os.path.join(os.path.expanduser('~'),  'Library', 'Preferences', 'com.matthewyang.NotepadEE')
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

make_new_instance = """#!/bin/bash

INSTANCES=~/Library/Caches/NotepadEE/Instances
CACHES=~/Library/Caches/NotepadEE
if [ ! -d "$CACHES" ]; then
  mkdir "$CACHES"
fi
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
cachefolder = os.path.join(os.path.expanduser('~'), 'Library', 'Caches', 'NotepadEE')
if not os.path.exists(cachefolder):
    os.makedirs(cachefolder)

with open(instanceshellscriptpath, "w") as f:
    f.write(make_new_instance)

root = tk.Tk()
ask_quit = False
root.title("Notepad==")
root.minsize(800, 600)
root.pack_propagate(False)

status_frame = tk.Frame(root)
status_frame.pack()

line_var = tk.StringVar()
line_label = tk.Label(status_frame, textvariable=line_var)
line_label.pack(side=tk.LEFT)

column_var = tk.StringVar()
column_label = tk.Label(status_frame, textvariable=column_var)
column_label.pack(side=tk.LEFT)

word_count_var = tk.StringVar()
word_count_label = tk.Label(status_frame, textvariable=word_count_var)
word_count_label.pack(side=tk.LEFT)

def get_font_for_platform():
    if os.name == 'nt':
        return font.Font(family="Consolas", size=12)
    elif os.uname().sysname == 'Darwin':
        return font.Font(family="Menlo", size=12)
    else:
        return font.Font(family="DejaVu Sans Mono", size=12)

text_font = get_font_for_platform()
text_area = tk.Text(root, width=100, height=80, wrap=tk.WORD, undo=True)
text_area.config(font=text_font)

def debug_var(event=None):
#    global file_open, current_file
#    if current_file:
#        print("Current file variable works")
#        print(current_file)
#    else:
#        print("Not intact")
#    if file_open:
#        print("File_open variable is intact")
#        print(file_open)
#    else:
#        print("Not working")
    return 'break'

def autosave_file(event=None):
    global current_file
    global file_open
    try:
        if file_open==1:
            with open(current_file, 'w') as file:
                text = text_area.get('1.0', 'end-1c')
                file.write(text)
    except FileNotFoundError:
        return 'break'

def write_cache(event=None):
    global current_file
    global file_open
    with open(os.path.join(os.path.expanduser('~'), 'Library', 'Preferences', 'com.matthewyang.NotepadEE', 'last_write'), 'w') as file:
        file.write(text_area.get('1.0', 'end-1c'))
    last_file_path = os.path.join(os.path.expanduser('~'), 'Library', 'Preferences', 'com.matthewyang.NotepadEE', 'last_file_path')
    with open(last_file_path, 'w') as file:
        file.write(current_file)
    autosave_file()

def save_as(event=None):
    global current_file, file_open
    file_path = filedialog.asksaveasfilename(defaultextension="")
    current_file=file_path
    if not file_path:
        return 'break'
    try:
        with open(file_path, 'w') as file:
            text = text_area.get(1.0, "end-1c")
            file.write(text)
        write_cache()
        file_open=1
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")

def open_file(event=None):
    global current_file, file_open
    file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    if not file_path:
        return 'break'
    try:
        with open(file_path, 'r') as file:
            text = file.read()  # Read the entire contents of the file
            text_area.delete(1.0, "end")  # Clear the current contents of text_area
            text_area.insert(1.0, text)  # Insert the read text into text_area
        write_cache()
        file_open=1
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    write_cache()

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

def new_file(event=None):
    global current_file, file_open
    text_area.delete(1.0, "end")
    current_file=""
    write_cache()
    file_open=0

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

def undo(event=None):
    try:
        text_area.edit_undo()
    except tk.TclError:
        pass

def redo(event=None):
    try:
        text_area.edit_redo()
    except tk.TclError:
        pass

def find_and_replace():
    popup = tk.Toplevel(root)
    popup.title("Find and Replace")

    find_label = tk.Label(popup, text="Enter the text you want to find:")
    find_label.pack()
    find_entry = tk.Entry(popup)
    find_entry.pack()

    replace_label = tk.Label(popup, text="Enter the text you want to it replace with:")
    replace_label.pack()
    replace_entry = tk.Entry(popup)
    replace_entry.pack()

    def perform_replace():
        find_text = find_entry.get()
        replace_text = replace_entry.get()

        text_widget = text_area.get("1.0", tk.END)
        if find_text:
            text_widget = text_widget.replace(find_text, replace_text)
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, text_widget)

        popup.destroy()

    replace_button = tk.Button(popup, text="Replace", command=perform_replace)
    replace_button.pack()

def add_instance(event=None):
  subprocess.run(["/bin/bash", instanceshellscriptpath])

def clear_instances(event=None):
    response2 = messagebox.askyesno("Clear instances", "Are you sure you want to clear all instances? Make sure to close all other instances before clearing. Click 'No' to get back to clear all other instances.")
    if response2:
        folder_path = os.path.join(os.path.expanduser('~'), 'Library', 'Caches', 'NotepadEE', 'Instances')
        shutil.rmtree(folder_path)

def update_line_number(event=None):
    line, column = text_area.index(tk.INSERT).split('.')
    line_var.set("Line: " + line)
    column_var.set("Column: " + column)
    words = text_area.get(1.0, 'end-1c').split()
    word_count_var.set("Words: " + str(len(words)))

def increase_font_size(event=None):
    current_size = text_font['size']
    text_font.config(size=current_size + 1)

def decrease_font_size(event=None):
    current_size = text_font['size']
    text_font.config(size=current_size - 1)

def runonkeyrelease(event=None):
    write_cache()
    update_line_number()

text_area.pack(fill=tk.BOTH, expand=tk.YES)
text_area.bind('<KeyRelease>', runonkeyrelease)
if os.path.exists(last_write):
    text_area.delete(1.0, "end")
    with open(last_write, 'r') as file:
        text_area.insert(1.0, file.read())

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save as...", command=save_as)

edit_menu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_command(label="Select All", command=select_all_text)
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_command(label="Redo", command=redo)
edit_menu.add_command(label="Find and Replace", command=find_and_replace)

accessibility_menu = tk.Menu(menu)
menu.add_cascade(label="Accessibility", menu=accessibility_menu)
accessibility_menu.add_command(label="Zoom in", command=increase_font_size)
accessibility_menu.add_command(label="Zoom out", command=decrease_font_size)

window_menu = tk.Menu(menu)
menu.add_cascade(label="Window", menu=window_menu)
window_menu.add_command(label="Launch new instance", command=add_instance)
window_menu.add_command(label="Clear all instances", command=clear_instances)

root.bind('<Command-n>', new_file)
root.bind('<Command-o>', open_file)
root.bind('<Command-s>', save_file)
root.bind('<Command-S>', save_as)

text_area.bind('<Command-x>', cut_text)
text_area.bind('<Command-c>', copy_text)
text_area.bind('<Command-v>', paste_text)
text_area.bind('<Command-a>', select_all_text)
text_area.bind('<Command-z>', undo)
text_area.bind('<Command-Z>', redo)

text_area.bind('<Command-equal>', increase_font_size)
text_area.bind('<Command-minus>', decrease_font_size)

root.bind('<Command-l>', add_instance)
root.bind('<Command-L>', clear_instances)

write_cache()
root.mainloop()
