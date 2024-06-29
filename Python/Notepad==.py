import tkinter as tk
from tkinter import filedialog
import os

last_file_path = os.path.join(os.path.expanduser('~'), 'Library', 'Caches', 'NotepadEE', 'last_file_path')
if os.path.exists(last_file_path):
    with open(last_file_path, 'r') as file:
        current_file = file.read()
else:
    current_file = ""
last_write=os.path.join(os.path.expanduser('~'), 'Library', 'Caches', 'NotepadEE', 'last_write')
folder_path = os.path.join(os.path.expanduser('~'), 'Library', 'Caches', 'NotepadEE')
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

def save_as():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    current_file=file_path
    with open(file_path, 'w') as file:
        text = text_area.get(1.0, "end-1c")
        file.write(text)

def open_file():
    global current_file
    file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    if file_path:
        text_area.delete(1.0, "end")
        current_file=file_path
        with open(file_path, 'r') as file:
            text_area.insert(1.0, file.read())

def save_file():
    global current_file
    if os.path.exists(current_file):
        with open(current_file, 'w') as file:
            text = text_area.get('1.0', 'end-1c')
            file.write(text)
    else:
        response = messagebox.askyesno("Create new file", "The file does not exist. Do you want to create a new file?")
        if response:
            with open(current_file, 'w') as file:
                text = text_area.get('1.0', 'end-1c')
                file.write(text)

def quit():
    global current_file
    with open(os.path.join(os.path.expanduser('~'), 'Library', 'Caches', 'NotepadEE', 'last_write'), 'w') as file:
        file.write(text_area.get('1.0', 'end-1c'))
    last_file_path = os.path.join(folder_path, 'last_file_path')
    with open(last_file_path, 'w') as file:
        file.write(current_file)
    root.destroy()

root = tk.Tk()
root.title("Notepad==")

text_area = tk.Text(root, width=100, height=80)
text_area.pack()
if os.path.exists(last_write):
    text_area.delete(1.0, "end")
    with open(last_write, 'r') as file:
        text_area.insert(1.0, file.read())

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save As...", command=save_as)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save", command=save_file)

edit_menu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: root.focus_get().event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: root.focus_get().event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: root.focus_get().event_generate("<<Paste>>"))
edit_menu.add_command(label="Select All", command=lambda: root.focus_get().event_generate("<<SelectAll>>"))

window_menu = tk.Menu(menu)
menu.add_cascade(label="Window", menu=window_menu)
window_menu.add_command(label="Close", command=quit)

root.mainloop()
