import sys
sys.path.append('/opt/lib/python3.11/site-packages')
import tkinter as tk
from tkinter import filedialog

def save_as():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    with open(file_path, 'w') as file:
        text = text_area.get(1.0, "end-1c")
        file.write(text)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        text_area.delete(1.0, "end")
        with open(file_path, 'r') as file:
            text_area.insert(1.0, file.read())

root = tk.Tk()
root.title("Notepad==")

text_area = tk.Text(root, width=100, height=80)
text_area.pack()

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save As...", command=save_as)
file_menu.add_command(label="Open...", command=open_file)

edit_menu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: root.focus_get().event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: root.focus_get().event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: root.focus_get().event_generate("<<Paste>>"))
edit_menu.add_command(label="Select All", command=lambda: root.focus_get().event_generate("<<SelectAll>>"))

root.mainloop()
