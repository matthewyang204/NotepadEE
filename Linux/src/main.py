import tkinter as tk
from tkinter import filedialog
import tklinenums as tkln
import os
from tkinter import messagebox
from tkinter import font
import sys
import time
import platform
import subprocess
import threading
# import atexit
import signal
import errno
try:
    import idlelib.colorizer as ic
    import idlelib.percolator as ip
    syntaxHighlighting = True
except ImportError:
    syntaxHighlighting = False
import re
import pathlib
import builtins
import traceback
import hashlib
import pyperclip
from common import *
from platformSpecific import *
import fileio
from fileio import *

root = tk.Tk()
ask_quit = False
root.title("Notepad==")
root.minsize(800, 600)
root.pack_propagate(False)

if platform.system() == "Windows":
    run_path = os.path.realpath(__file__)
    runDir = os.path.dirname(run_path)
    app_icon = os.path.join(runDir, 'Notepad.ico')
    root.iconbitmap(app_icon)

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

text_size_indicator = tk.StringVar()
size_label = tk.Label(status_frame, textvariable=text_size_indicator)
size_label.pack(side=tk.LEFT)

file_var = tk.StringVar()
file_label = tk.Label(status_frame, textvariable=file_var)
file_label.pack(side=tk.LEFT)

text_frame = tk.Frame(root)
text_frame.pack(fill=tk.BOTH, expand=True)

def get_font_for_platform():
    if os.name == 'nt':
        return font.Font(family="Consolas", size=12)
    elif os.uname().sysname == 'Darwin':
        return font.Font(family="Menlo", size=12)
    else:
        return font.Font(family="DejaVu Sans Mono", size=12)

text_font = get_font_for_platform()
text_area = tk.Text(text_frame, width=100, height=80, wrap=tk.WORD, undo=True)
text_area.config(font=text_font)
fileio.text_area = text_area

if syntaxHighlighting:
    try:
        cdg = ic.ColorDelegator()
        cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat().pattern, re.S)
        cdg.idprog = re.compile(r'\s+(\w+)', re.S)

        cdg.tagdefs['MYGROUP'] = {'foreground': '#7F7F7F', 'background': ''}
        
        # For platforms with malfunctioning idlelibs, force the standard colors
        if platform.system() == "Darwin":
            cdg.tagdefs['COMMENT']    = {'foreground': '#dd0000', 'background': ''}  # red
            cdg.tagdefs['KEYWORD']    = {'foreground': '#F2A061', 'background': ''}  # orange
            cdg.tagdefs['BUILTIN']    = {'foreground': '#900090', 'background': ''}  # purple
            cdg.tagdefs['STRING']     = {'foreground': '#00aa00', 'background': ''}  # green
            cdg.tagdefs['DEFINITION'] = {'foreground': '#000000', 'background': ''}  # black
    except AttributeError:
        cdg = ic.ColorDelegator()
        cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat(), re.S)
        cdg.idprog = re.compile(r'\s+(\w+)', re.S)

        cdg.tagdefs['MYGROUP'] = {'foreground': '#7F7F7F', 'background': ''}
        
        # For platforms with malfunctioning idlelibs, force the standard colors
        if platform.system() == "Darwin":
            cdg.tagdefs['COMMENT']    = {'foreground': '#dd0000', 'background': ''}  # red
            cdg.tagdefs['KEYWORD']    = {'foreground': '#F2A061', 'background': ''}  # orange
            cdg.tagdefs['BUILTIN']    = {'foreground': '#900090', 'background': ''}  # purple
            cdg.tagdefs['STRING']     = {'foreground': '#00aa00', 'background': ''}  # green
            cdg.tagdefs['DEFINITION'] = {'foreground': '#000000', 'background': ''}  # black
else:
    printlog("Platform does not support newer idlelibs, syntax highlighting is disabled")

text_area.delete(1.0, "end")
with open(last_write, 'r') as file:
    text_area.insert(1.0, file.read())
if platform.system() == "Darwin" or platform.system() == "Linux":
    printlog("Clearing any locks...")
    subprocess.call(["/bin/rm", "-rf", os.path.join(cache_path, "loadPreviousSave.lock")])
else:
    printlog("We are on a system that does not need or use file locks, skipping...")

tab_mode = tk.StringVar(value="tab")
ogCursorColor = text_area.cget("fg")



class text_scroll():
    def to_cursor(event=None):
        text_area.see("insert")
    
    def to_position(position):
        text_area.see(position)

def cut_text(event=None):
    pyperclip.copy(text_area.get("sel.first", "sel.last"))
    text_area.delete("sel.first", "sel.last")
    printlog("Cut option succeeded")
    return 'break'

def copy_text(event=None):
    pyperclip.copy(text_area.get("sel.first", "sel.last"))
    printlog("Text copied to clipboard")
    return 'break'


def paste_text(event=None):
    text_area.insert("insert", pyperclip.paste())
    printlog("Text pasted from clipboard")
    return 'break'


def select_all_text(event=None):
    text_area.tag_add("sel", "1.0", "end")
    printlog("Text selected")
    return 'break'


def undo(event=None):
    try:
        text_area.edit_undo()
    except tk.TclError:
        pass
    printlog("Edit undone")


def redo(event=None):
    try:
        text_area.edit_redo()
    except tk.TclError:
        pass
    printlog("Edit redone")


def find_and_replace(event=None):
    popup = tk.Toplevel(root)
    popup.title("Find and Replace")

    find_label = tk.Label(popup, text="Enter the text you want to find:")
    find_label.pack()
    find_entry = tk.Entry(popup)
    find_entry.pack()

    replace_label = tk.Label(
        popup, text="Enter the text you want to replace it with:")
    replace_label.pack()
    replace_entry = tk.Entry(popup)
    replace_entry.pack()

    def perform_replace(event=None):
        find_text = find_entry.get()
        replace_text = replace_entry.get()

        text_widget = text_area.get("1.0", tk.END)
        if find_text:
            text_widget = text_widget.replace(find_text, replace_text)
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, text_widget)

    def close(event=None):
        popup.destroy()

    replace_button = tk.Button(popup, text="Replace", command=perform_replace)
    close_button = tk.Button(popup, text="Close", command=close)
    replace_button.pack()
    close_button.pack()
    find_entry.bind('<Return>', perform_replace)
    replace_entry.bind('<Return>', perform_replace)

def go_to_line(event=None):
    popup = tk.Toplevel(root)
    popup.title("Go To Line")
    
    line_number_label = tk.Label(popup, text="Enter the line that you want to go to:")
    line_number_label.pack()
    entrybox = tk.Entry(popup)
    entrybox.pack()

    def go(event=None):
        line_number = entrybox.get()
        text_area.mark_set("insert", str(line_number) + ".0")
        text_scroll.to_cursor()

    def close(event=None):
        popup.destroy()
    
    go_to_line_button = tk.Button(popup, text="Go", command=go)
    close_button = tk.Button(popup, text="Close", command=close)
    go_to_line_button.pack()
    close_button.pack()
    entrybox.bind('<Return>', go)

def cPos(index):
    line, column = text_area.index("insert").split(".")

    if index == "both":
        return line, column
    elif index == "line":
        return line
    elif index == "column":
        return column
    else:
        printlog("invalidArg")
        return "invalidArg"

def findNext(text):
    try:
        last_highlight = text_area.index("highlight.last")
        start = last_highlight
    except tk.TclError:
        cPos_line, cPos_column = cPos("both")
        start = str(cPos_line) + "." + str(cPos_column)
        # start= "1.0"

    text_area.tag_remove("highlight", "1.0", "end")
    try:
        start = text_area.search(text, start, stopindex="end")
        end = str(start) + " + " + str(len(text)) + "c"
        text_area.tag_add("highlight", start, end)
    except Exception as e:
        start = "1.0"
        start = text_area.search(text, start, stopindex="end")
        end = str(start) + " + " + str(len(text)) + "c"
        text_area.tag_add("highlight", start, end)
    
    text_area.tag_config("highlight", background="yellow")
    text_area.mark_set("insert", end)
    text_scroll.to_position(start)

def find_text(event=None):
    popup = tk.Toplevel(root)
    popup.title("Find")
    
    line_number_label = tk.Label(popup, text="Enter the text that you want to find:")
    line_number_label.pack()
    entrybox = tk.Entry(popup)
    entrybox.pack()

    def findNext_wrapper(event=None):
        findNext(entrybox.get())

    def clear(event=None):
        text_area.tag_remove("highlight", "1.0", "end")

    def close(event=None):
        clear()
        popup.destroy()
    
    find_button = tk.Button(popup, text="Find Next", command = findNext_wrapper)
    close_button = tk.Button(popup, text="Close", command=close)
    clear_button = tk.Button(popup, text="Clear", command=clear)
    find_button.pack()
    clear_button.pack()
    close_button.pack()
    popup.protocol('WM_DELETE_WINDOW', close)
    entrybox.bind('<Return>', findNext_wrapper)
    
def mark_text(event=None):
    selectStart = text_area.index("sel.first")
    selectEnd = text_area.index("sel.last")
    # DO NOT enable this
    # printlog(f"Current selection is {selectStart}, {selectEnd}")
    printlog("Clearing all current highlights in selection...")
    text_area.tag_remove("highlight_permanent", selectStart, selectEnd)
    printlog("Configuring highlight_permanent tags to selection...")
    text_area.tag_add("highlight_permanent", selectStart, selectEnd)
    printlog("Configuring tagged text to highlight...")
    text_area.tag_config("highlight_permanent", background="green")
    printlog("done")
    
def unmark_text(event=None):
    selectStart = text_area.index("sel.first")
    selectEnd = text_area.index("sel.last")
    # DO NOT enable this
    # printlog(f"Current selection is {selectStart}, {selectEnd}")
    printlog("Clearing all current highlights in selection...")
    text_area.tag_remove("highlight_permanent", selectStart, selectEnd)
    printlog("done")

def unmark_all_text(event=None):
    printlog("Clearing all current highlights...")
    text_area.tag_remove("highlight_permanent", "1.0", "end")
    printlog("done")

def update_line_number(event=None):
    line, column = text_area.index(tk.INSERT).split('.')
    # line_var.set("Line: " + line)
    # column_var.set("Column: " + column)
    words = text_area.get(1.0, 'end-1c').split()
    word_count_var.set("Words: " + str(len(words)))
    file_var.set("File: " + os.path.basename(current_file))
    if current_file:
        root.title(str(current_file) + " - Notepad==") # f"{current_file} - Notepad=="
    else:
        root.title("Notepad==")
    text_size = text_font['size']
    text_size_indicator.set("Size: " + str(text_size)) # f"Size: {text_size}"
    linenums.linenums.redraw()
    # print("Status bar updated")
    root.after(100, update_line_number)

def applySyntaxHighlighting(event=None):
    global current_file, syntaxHighlighting
    pythonExts = ['.py', '.pyw', '.pyc', '.pyo', '.pyd', '.pyx', '.pxd', '.pxi', '.pyi', '.ipynb', '.pyz']
    if syntaxHighlighting:
        try:
            if pathlib.Path(os.path.basename(current_file)).suffix in pythonExts:
                ip.Percolator(text_area).insertfilter(cdg)
            else:
                if getattr(cdg, 'delegate', None) is not None:
                    ip.Percolator(text_area).removefilter(cdg)
        except Exception as e:
            if getattr(cdg, 'delegate', None) is not None:
                ip.Percolator(text_area).removefilter(cdg)
        
    else:
        printlog("Python version does not support syntax highlighting")

def increase_font_size(event=None):
    current_size = text_font['size']
    text_font.config(size=current_size + 1)
    printlog("Font size increased by 1 pt")

def decrease_font_size(event=None):
    current_size = text_font['size']
    text_font.config(size=current_size - 1)
    printlog("Font size decreased by 1 pt")

# Create a function to check for text in text_area
def check_file_written(event=None):
    global file_written
    printlog("Checking if text_area has been edited by the user to contain text...")
    current_text = text_area.get(1.0, "end-1c")
    # if there is text, set it to 1
    if current_text:
        printlog("There is text; setting to 1")
        file_written = 1
    # otherwise, set it to 0
    else:
        printlog("No text")
        file_written = 0

def runinbackground(event=None):
    write_prefs()
    check_file_written()
    applySyntaxHighlighting()
    debug_var()
    updateCursorColor()

class nw():
    def macOS(openFile=""):
        global folder_path
        if platform.system() == "Darwin":
            run_path = os.path.realpath(__file__)
            cwd = os.getcwd()
            freeze_time = 1
            emptyString = ""
            # printlog(f"Script path is {run_path}")
            # printlog(f"Current working directory is {cwd}")
            # printlog(f"App is located at {cwd}/Notepad==.app")
            # DO NOT enable this
            # printlog(f"Creating a lock file at {os.path.join(cache_path, "loadPreviousSave.lock")}...")
            with open(os.path.join(cache_path, "loadPreviousSave.lock"), "w", encoding='utf-8') as file:
                file.write(emptyString)
            # DO NOT enable this
            # printlog(f"Clearing the prefs folder at {folder_path} to ensure new instance loads up with new file...")
            subprocess.call(["/bin/rm", "-rf", folder_path])
            printlog("Launching new instance...")
            if openFile:
                subprocess.call(["/usr/bin/open", "-n", "-a", cwd + "/Notepad==.app", openFile])
            else:
                subprocess.call(["/usr/bin/open", "-n", "-a", cwd + "/Notepad==.app"])
            # DO NOT enable this
            # printlog(f"Waiting for {os.path.join(cache_path, "loadPreviousSave.lock")}...")
            while os.path.exists(os.path.join(cache_path, "loadPreviousSave.lock")):
                pass
            # DO NOT enable this
            # printlog(f"Writing cache back to prefs folder at {folder_path}...")
            write_prefs()
            printlog("done")
        else:
            raise platformError("This function is only designed to be run on macOS. We do not understand why you would want this function to run anyway, nor how you got it to run. The function needs to be specific to the platform.")

    def Linux(openFile=""):
        def main(event=None):
            global folder_path
            run_path = os.path.realpath(__file__)
            cwd = os.getcwd()
            pyexe = sys.executable
            pyexe_dir = os.path.dirname(pyexe)
            pyInstFile = os.path.join(pyexe_dir, '.pyinstaller')
            freeze_time = 1

            # DO NOT enable
            # printlog(f"Script path is {run_path}")
            # printlog(f"Current working directory is {cwd}")
            # printlog(f"Executable is located at {pyexe}")
            emptyString = ""

            # DO NOT enable, this is only compatible with Python 3.12 and later
            # printlog(f"Creating a lock file at {os.path.join(cache_path, "loadPreviousSave.lock")}...")
            with open(os.path.join(cache_path, "loadPreviousSave.lock"), "w", encoding='utf-8') as file:
                file.write(emptyString)
            # DO NOT enable
            # printlog(f"Clearing the prefs folder at {folder_path} to ensure new instance loads up with new file...")
            subprocess.call(["/bin/rm", "-rf", folder_path])
            printlog("Launching new instance...")
            # Regular launcher with no open file support
            def launcher():
                if os.path.exists(pyInstFile):
                    printlog("We are running in PyInstaller mode, running only the executable...")
                    subprocess.Popen([pyexe], preexec_fn=os.setsid, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
                else:
                    printlog("We are probably running in standard interpreted mode, launching executable with python file...")
                    subprocess.Popen([pyexe, run_path], preexec_fn=os.setsid, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
            # launcher with open file support
            def launcher2():
                if os.path.exists(pyInstFile):
                    printlog("We are running in PyInstaller mode, running only the executable...")
                    subprocess.Popen([pyexe, openFile], preexec_fn=os.setsid, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
                else:
                    printlog("We are probably running in standard interpreted mode, launching executable with python file...")
                    subprocess.Popen([pyexe, run_path, openFile], preexec_fn=os.setsid, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
            if openFile:
                launcher_thread = threading.Thread(target=launcher2)
            else:
                launcher_thread = threading.Thread(target=launcher)
            launcher_thread.start()
            # DO NOT enable, this is only compatible with Python 3.12 and later
            # printlog(f"Waiting for {os.path.join(cache_path, "loadPreviousSave.lock")}...")
            while os.path.exists(os.path.join(cache_path, "loadPreviousSave.lock")):
                pass
            # DO NOT enable
            # printlog(f"Writing cache back to prefs folder at {folder_path}...")
            write_prefs()
            printlog("done")
        if platform.system() == "Linux":
            main()
        else:
            raise platformError("This function is only designed to be run on Linux. We do not understand why you would want this function to run anyway, nor how you got it to run. The function needs to be specific to the platform.")

def newWindow(event=None):
    if platform.system() == "Darwin":
        threading.Thread(target=nw.macOS(), daemon=True).start()
    elif platform.system() == "Linux":
        nw.Linux()
    elif platform.system() == "Windows":
        new_file()
    else:
        raise platformError("There is no newWindow function available for your platform.")

def exit_handler(event=None):
    printlog("Telling user to save file before exit...")
    if save_file("w"):
        printlog("Exiting...")
        sys.exit()
    else:
        printlog("User pressed cancel, not exiting...")

def exit_on_keyboardInterrupt(signum, frame):
    printlog("Received KeyboardInterrupt, running exit handler...")
    exit_handler()

class edit_menu_funcs():
    def show_edit_context_menu(event=None):
        edit_context_menu.tk_popup(event.x_root, event.y_root)
    def hide_edit_context_menu(event=None):
        edit_context_menu.unpost()

class lineNumbers:
    def __init__(self):
        self.linenums = tkln.TkLineNumbers(text_frame, text_area, justify="center")
        self.linenums.pack(side="left", fill="y")

    def scrollBoth(self, *args):
        text_area.yview(*args)
        self.linenums.yview(*args)

    def updateScroll(self, first, last):
        scrollbar.set(first, last)
        self.linenums.yview_moveto(first)
        self.linenums.redraw()
linenums = lineNumbers()

def updateCursorColor(event=None):
    global ogCursorColor
    tags = text_area.tag_names("insert")
    if "highlight" in tags:
        text_area.config(insertbackground="blue")
    elif "highlight_permanent" in tags:
        text_area.config(insertbackground="magenta")
    else:
        text_area.config(insertbackground=ogCursorColor)

class keyShortcuts:
    def insert_tab(event=None):
        if tab_mode.get() == "tab":
            text_area.insert("insert", "\t")
        elif tab_mode.get() == "spaces":
            text_area.insert("insert", "    ")
        return 'break'

    text_area.bind("<Tab>", insert_tab)

class about():
    def about(event=None):
        messagebox.showinfo("About Notepad==", versionInfo)

    def show_license(event=None):
        messagebox.showinfo("License", "This program is licensed under the GNU GPLv3. If you did not receive a copy with this program, go to https://github.com/matthewyang204/NotepadEE or read the LICENSE file in your copy of the source code.")

scrollbar = tk.Scrollbar(text_frame, orient="vertical", command=text_area.yview)
scrollbar.config(command=linenums.scrollBoth)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area.config(yscrollcommand=linenums.updateScroll)

text_area.pack(fill=tk.BOTH, expand=tk.YES, side=tk.LEFT)
text_area.bind('<KeyRelease>', runinbackground)
text_area.bind('<Button-1>', runinbackground)
runinbackground()
update_line_number()

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=newWindow)
file_menu.add_command(label="Open...", command=open_file_v2)
file_menu.add_command(label="Save", command=save_file2)
file_menu.add_command(label="Save as...", command=save_as)
if not platform.system() == "Darwin":
    file_menu.add_command(label="Quit", command=exit_handler)

edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
# edit_menu.add_command(label="Jump To Cursor [Debug]", command=text_scroll.to_cursor)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
edit_menu.add_command(label="Select All", command=select_all_text)
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_command(label="Redo", command=redo)
edit_menu.add_separator()
edit_menu.add_command(label="Mark Text", command=mark_text)
edit_menu.add_command(label="Unmark Text", command=unmark_text)
edit_menu.add_command(label="Unmark All Text", command=unmark_all_text)
edit_menu.add_separator()
edit_menu.add_command(label="Find", command=find_text)
edit_menu.add_command(label="Find and Replace", command=find_and_replace)
edit_menu.add_separator()
edit_menu.add_command(label="Go To Line", command=go_to_line)

accessibility_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Accessibility", menu=accessibility_menu)
accessibility_menu.add_command(label="Zoom in", command=increase_font_size)
accessibility_menu.add_command(label="Zoom out", command=decrease_font_size)

tool_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Tools", menu=tool_menu)
# Begin tab modes submenu
tab_modes_menu = tk.Menu(tool_menu, tearoff=0)
tool_menu.add_cascade(label="Tab Modes", menu=tab_modes_menu)
tab_modes_menu.add_radiobutton(label="Tab", variable=tab_mode, value="tab")
tab_modes_menu.add_radiobutton(label="Spaces", variable=tab_mode, value="spaces")
# End tab modes submenu

window_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Window", menu=window_menu)
window_menu.add_command(label="Close", command=exit_handler)

help_menu = tk.Menu(menu, tearoff=0)
about_menu = help_menu
menu.add_cascade(label="Help", menu=help_menu)
about_menu.add_command(label="About Notepad==", command=about.about)
about_menu.add_command(label="License", command=about.show_license)

# Separate context menus not linked to menu bar
edit_context_menu = tk.Menu(root, tearoff=0)
edit_context_menu.add_command(label="Cut", command=cut_text)
edit_context_menu.add_command(label="Copy", command=copy_text)
edit_context_menu.add_command(label="Paste", command=paste_text)
edit_context_menu.add_command(label="Select All", command=select_all_text)
edit_context_menu.add_separator()
edit_context_menu.add_command(label="Undo", command=undo)
edit_context_menu.add_command(label="Redo", command=redo)
edit_context_menu.add_separator()
edit_context_menu.add_command(label="Mark Text", command=mark_text)
edit_context_menu.add_command(label="Unmark Text", command=unmark_text)
edit_context_menu.add_command(label="Unmark All Text", command=unmark_all_text)

if platform.system() == "Darwin":
    root.bind_all("<Command-w>", exit_handler)
else:
    root.bind_all("<Control-w>", exit_handler)

if platform.system() == "Darwin":
    root.bind_all('<Command-n>', newWindow)
    root.bind_all('<Command-N>', newWindow)
    root.bind_all('<Command-o>', open_file_v2)
    root.bind_all('<Command-s>', save_file)
    root.bind_all('<Command-S>', save_as)
else:
    root.bind_all('<Control-n>', newWindow)
    root.bind_all('<Control-N>', newWindow)
    root.bind_all('<Control-o>', open_file_v2)
    root.bind_all('<Control-s>', save_file)
    root.bind_all('<Control-S>', save_as)

if platform.system() == "Darwin":
    text_area.bind('<Command-x>', cut_text)
    text_area.bind('<Command-c>', copy_text)
    text_area.bind('<Command-v>', paste_text)
    text_area.bind('<Command-a>', select_all_text)
    text_area.bind('<Command-z>', undo)
    text_area.bind('<Command-Z>', redo)
    text_area.bind('<Command-m>', mark_text)
    text_area.bind('<Command-M>', unmark_text)
    text_area.bind('<Command-U>', unmark_all_text)
    text_area.bind('<Command-f>', find_text)
    text_area.bind('<Command-R>', find_and_replace)
    text_area.bind('<Command-G>', go_to_line)
else:
    text_area.bind('<Control-x>', cut_text)
    text_area.bind('<Control-c>', copy_text)
    text_area.bind('<Control-v>', paste_text)
    text_area.bind('<Control-a>', select_all_text)
    text_area.bind('<Control-z>', undo)
    text_area.bind('<Control-y>', redo)
    text_area.bind('<Control-m>', mark_text)
    text_area.bind('<Control-M>', unmark_text)
    text_area.bind('<Control-U>', unmark_all_text)
    text_area.bind('<Control-f>', find_text)
    text_area.bind('<Control-R>', find_and_replace)
    text_area.bind('<Control-G>', go_to_line)

if platform.system() == "Darwin":
    text_area.bind('<Command-equal>', increase_font_size)
    text_area.bind('<Command-minus>', decrease_font_size)
else:
    text_area.bind('<Control-equal>', increase_font_size)
    text_area.bind('<Control-minus>', decrease_font_size)

text_area.bind('<Button-3>', edit_menu_funcs.show_edit_context_menu)
text_area.bind("<Control-Button-1>", edit_menu_funcs.show_edit_context_menu)
# text_area.bind('<Button-1>', edit_menu_funcs.hide_edit_context_menu)

# atexit.register(exit_handler)
signal.signal(signal.SIGINT, exit_on_keyboardInterrupt)
signal.signal(signal.SIGTERM, exit_on_keyboardInterrupt)
root.protocol('WM_DELETE_WINDOW', exit_handler)

# Implement quit event if macOS
if platform.system() == "Darwin":
    root.createcommand('::tk::mac::Quit', exit_handler)
else:
    root.bind_all("<Control-q>", exit_handler)

write_prefs()
root.mainloop()
