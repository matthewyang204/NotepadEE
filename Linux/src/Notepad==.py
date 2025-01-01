import tkinter as tk
from tkinter import filedialog
import os
from tkinter import messagebox
from tkinter import font
import sys
import time
import platform
import subprocess

cache_path = os.path.join(os.path.expanduser('~'), '.notepadee', 'cache')
if not os.path.exists(cache_path):
    os.makedirs(cache_path)

# Open a log file in write mode
log_file = os.path.join(cache_path, "notepadee_log.txt")

# Special printlog statement to print stuff that doesn't belong in a console to the log file
def printlog(message):
    with open(log_file, 'a') as file:
        file.write(message + '\n')
    print(message)

global fileToBeOpened
global openFile
fileToBeOpened = None
openFile = None

def debug_NS_var():
    printlog("fileToBeOpened = " + str(fileToBeOpened))
    printlog("openFile = " + str(openFile))

# Check if the system is macOS (Darwin)
if platform.system() == "Darwin":
    import objc
    from AppKit import NSApplication
    import AppKit

    # Dummy monkey patch functions
    def dummy_macOSVersion(self):
        printlog("Intercepted call to macOSVersion!")
        return None

    def patched_setup(self, arg):
        printlog("Intercepted _setup method call!")
        try:
            return original_setup(self)
        except Exception as e:
            printlog(f"Error in patched _setup: {e}")
            return None

    # Set monkey patches to run
    objc.classAddMethod(NSApplication, b"macOSVersion", dummy_macOSVersion)
    AppKit.NSApplication._setup_ = patched_setup

    from Cocoa import NSApplication, NSApp, NSObject
    from Foundation import NSURL
    # Tell the user in the console that it is running from macOS
    printlog("Detected that we are running on macOS, retrieving filepath through Finder's proprietary Cocoa APIs...")
    # macOS logic to fetch the Finder file path
    try:
        class AppDelegate(NSObject):
            def applicationDidFinishLaunching_(self, notification):
                pass

            def applicationOpenFile_(self, filePath):
                global fileToBeOpened, openFile
                if not str(filePath): # no file path provided
                    # Handle the case where no file is passed, like launching from dock
                    fileToBeOpened = ""
                    openFile = 0
                    debug_NS_var()
                    printlog("No file selected in Finder, loading program with last known file...")
                else:
                    # File path is passed, take the file
                    fileToBeOpened = str(filePath)
                    openFile = 1
                    debug_NS_var()
                    printlog("File was passed through Finder, opening file...")

                return True
        
        def retrieve():
            global fileToBeOpened, openFile
            app_delegate = AppDelegate()
            app = NSApplication.sharedApplication()
            app.setDelegate_(app_delegate)
            app.run
        
        retrieve()

    except Exception as e:
        fileToBeOpened = ""
        openFile = 0
        debug_NS_var()
        printlog(str(e))
        printlog("No file selected in Finder, loading program with last known file...")
else:
    # Tell the user through the console that we are running on Linux
    printlog("We are running on a standard Linux distro or other OS, falling back to file arguments...")
    # If not macOS, fallback to command line arguments
    filearg = sys.argv
    if len(filearg) <= 1:
        openFile = 0
        printlog("No arguments provided. Proceeding to load program with last known file...")
    else:
        openFile = 1
        printlog("Assuming argument is the file to open. Loading file...")
        fileToBeOpened = filearg[1]

global file_open
file_open = 0
last_file_path = os.path.join(os.path.expanduser('~'), '.notepadee', 'prefs',
                              'last_file_path')
if os.path.exists(last_file_path):
    with open(last_file_path, 'r') as file:
        current_file = file.read()
        if current_file.strip() == '':  # Check if the file is empty
            file_open = 0
        else:
            file_open = 1

else:
    current_file = ""
    file_open = 0

folder_path = os.path.join(os.path.expanduser('~'), '.notepadee', 'prefs')
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

global last_write
last_write = os.path.join(os.path.expanduser('~'), '.notepadee', 'prefs', 'last_write')
if not os.path.exists(last_write):
    with open(last_write, 'w'):
        pass

file_written = 0
printlog("file_written set to " + str(file_written))

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

text_area.delete(1.0, "end")
with open(last_write, 'r') as file:
    text_area.insert(1.0, file.read())
printlog("Program loaded")

def debug_var(event=None):
    global file_open, current_file
    if current_file:
        printlog("Current file variable works")
        printlog(current_file)
    else:
        printlog("Not intact")
    if file_open:
        printlog("File_open variable is intact")
        printlog(file_open)
    else:
        printlog("Not working")
    return 'break'


def autosave_file(event=None):
    global current_file
    global file_open
    try:
        if file_open == 1:
            with open(current_file, 'w') as file:
                text = text_area.get('1.0', 'end-1c')
                file.write(text)
    except FileNotFoundError:
        return 'break'
    printlog("Autosaved file")


def write_prefs(event=None):
    global current_file, file_open
    with open(
            os.path.join(os.path.expanduser('~'), '.notepadee', 'prefs',
                         'last_write'), 'w') as file:
        file.write(text_area.get('1.0', 'end-1c'))
    last_file_path = os.path.join(os.path.expanduser('~'), '.notepadee',
                                  'prefs', 'last_file_path')
    with open(last_file_path, 'w') as file:
        file.write(str(current_file))
    autosave_file()
    printlog("Wrote prefs successfully")


# save_as provides the dialog
def save_as(event=None):
    global current_file, file_open
    file_path = filedialog.asksaveasfilename(
        defaultextension="",
        filetypes=(
            ("All Files", "*.*"),

            # Notepad files
            ("Plain text file", ".txt"),
            ("Log file", ".log"),

            # ms ini/inf
            ("INI file", ".ini"),
            ("INF file (.inf)", ".inf"),

            # C, C++, objc
            ("C, C++, objc header", ".h"),
            ("C, C++, objc header", ".hh"),
            ("C, C++, objc header", ".hpp"),
            ("C, C++, objc header", ".hxx"),
            ("C, C++, objc source", ".c"),
            ("C, C++, objc source", ".cpp"),
            ("C, C++, objc source", ".cxx"),
            ("C, C++, objc source", ".cc"),
            ("C, C++, objc source", ".m"),
            ("C, C++, objc source", ".mm"),
            ("C, C++, objc project", ".vcxproj"),
            ("C, C++, objc project", ".vcproj"),
            ("C, C++, objc properties", ".props"),
            ("C, C++, objc properties", ".vsprops"),
            ("C, C++, objc manifest", ".manifest"),

            # Java, C#, Pascal
            ("Java file", ".java"),
            ("C# file", ".cs"),
            ("Pascal file", ".pas"),
            ("Pascal file", ".pp"),
            ("Include file", ".inc"),

            # Web script files
            ("HTML file", ".html"),
            ("HTML file", ".htm"),
            ("Server-side HTML", ".shtml"),
            ("Server-side HTML", ".shtm"),
            ("HTML Application", ".hta"),
            ("ASP file", ".asp"),
            ("ASP.NET file", ".aspx"),
            ("CSS file", ".css"),
            ("JavaScript file", ".js"),
            ("JSON file", ".json"),
            ("JavaScript module", ".mjs"),
            ("JavaScript module", ".jsm"),
            ("JSP file", ".jsp"),
            ("PHP file", ".php"),
            ("PHP3 file", ".php3"),
            ("PHP4 file", ".php4"),
            ("PHP5 file", ".php5"),
            ("PHP script", ".phps"),
            ("PHP script", ".phpt"),
            ("PHP file", ".phtml"),
            ("XML file", ".xml"),
            ("XHTML file", ".xhtml"),
            ("XHTML file", ".xht"),
            ("XUL file", ".xul"),
            ("KML file", ".kml"),
            ("XAML file", ".xaml"),
            ("XSML file", ".xsml"),

            # Script files
            ("Shell script", ".sh"),
            ("Bash script", ".bsh"),
            ("Bash script", ".bash"),
            ("Batch file", ".bat"),
            ("Command file", ".cmd"),
            ("NSIS script", ".nsi"),
            ("NSIS header", ".nsh"),
            ("Lua script", ".lua"),
            ("Perl script", ".pl"),
            ("Perl module", ".pm"),
            ("Python script", ".py"),
            ("Inno Setup script", ".iss"),

            # Property scripts
            ("Resource file", ".rc"),
            ("ActionScript", ".as"),
            ("MaxScript", ".mx"),
            ("Visual Basic", ".vb"),
            ("Visual Basic script", ".vbs"),

            # Fortran, TeX, SQL
            ("Fortran file", ".f"),
            ("Fortran file", ".for"),
            ("Fortran 90 file", ".f90"),
            ("Fortran 95 file", ".f95"),
            ("Fortran 2000 file", ".f2k"),
            ("TeX file", ".tex"),
            ("SQL file", ".sql"),

            # Miscellaneous files
            ("NFO file", ".nfo"),
            ("Makefile", ".mak")))
    current_file = file_path
    # if file_path doesn't exist, let's stop the function and return False
    if not file_path:
        return False
    
    # if we get a valid file_path, let's save via dialog
    try:
        printlog("Saving file to location:")
        printlog(file_path)
        with open(file_path, 'w') as file:
            text = text_area.get(1.0, "end-1c")
            file.write(text)
        write_prefs()
        file_open = 1
        printlog("File was saved to different location successfully.")
        return True
    
    # if any errors manage to get past this, let's do an exception to quit gracefully
    except FileNotFoundError:
        messagebox.showerror("Error", "Location nonexistent")
        return False

def open_file(event=None):
    global current_file, file_open
    save_file("y")
    file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    if file_path:
        text_area.delete(1.0, "end")
        current_file = file_path
        with open(file_path, 'r') as file:
            text_area.insert(1.0, file.read())
        file_open = 1
        printlog("New file opened")
    write_prefs()


def save_file(warn):
    global current_file, file_open
    if file_open == 1:
        try:
            debug_var()
            with open(current_file, 'w') as file:
                text = text_area.get('1.0', 'end-1c')
                file.write(text)
            write_prefs()
            return True
        except FileNotFoundError:
            return 'break'
    else:
        if warn == "y":
            response = messagebox.askyesno("Warning: File is not saved","The current file is not saved. Do you want to save it to a selected location?")
            if response:
                if save_as():
                    printlog("File saved without warning")
                    return True
            else:
                return True
        else:
            response = messagebox.askyesno("Create new file","The file does not exist. Do you want to create it as a new file before proceeding?")
            if response:
                if save_as():
                    printlog("File saved after warning user")
                    return True
            else:
                return True

def save_file2(event=None):
    global current_file, file_open, file_written
    printlog("No-warning wrapper triggered, running save_file with nowarning option")
    save_file("n")

def new_file(event=None):
    global current_file, file_open, file_written

    # Check if there is text in text_area
    if file_written == 1:
        # Only run this code if save_file, otherwise, don't force user to clear
        if save_file("y"):
            text_area.delete(1.0, "end")
            printlog("Cleared text_area")
            current_file = ""
            write_prefs()
            file_open = 0
            printlog("New file created")
            file_written = 0
    
    # Otherwise, clear without obstruction
    else:
        text_area.delete(1.0, "end")
        printlog("Cleared text_area")
        current_file = ""


def cut_text(event=None):
    text_area.clipboard_clear()
    text_area.clipboard_append(text_area.get("sel.first", "sel.last"))
    text_area.delete("sel.first", "sel.last")
    printlog("Cut option succeeded")
    return 'break'


def copy_text(event=None):
    text_area.clipboard_clear()
    text_area.clipboard_append(text_area.get("sel.first", "sel.last"))
    printlog("Text copied to clipboard")
    return 'break'


def paste_text(event=None):
    text_area.insert("insert", text_area.clipboard_get())
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


def find_and_replace():
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


def update_line_number(event=None):
    line, column = text_area.index(tk.INSERT).split('.')
    line_var.set("Line: " + line)
    column_var.set("Column: " + column)
    words = text_area.get(1.0, 'end-1c').split()
    word_count_var.set("Words: " + str(len(words)))
    # printlog("Status bar updated")
    root.after(100, update_line_number)

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
    debug_var()

def runonfilearg(file_path):
    global file_open, current_file
    if os.path.exists(file_path):
        text_area.delete(1.0, "end")
        current_file = os.path.abspath(file_path)
        with open(file_path, 'r') as file:
            text_area.insert(1.0, file.read())
        write_prefs()
        file_open = 1
        #printlog("Current file path: " + current_file)
        #printlog("File open: " + str(file_open))
        printlog("File loaded")
    else:
        text_area.delete(1.0, "end")
        with open(file_path, 'w') as file:
            text = text_area.get(1.0, "end-1c")
            file.write(text)
        file_open = 1
        current_file = os.path.abspath(file_path)
        #printlog("Current file path: " + current_file)
        #printlog("File open: " + str(file_open))
        write_prefs()
        printlog("Because the file doesn't exist, it was created as a blank new file instead")

if openFile == 1:
    runonfilearg(fileToBeOpened)
else:
    printlog("Program loaded")
text_area.pack(fill=tk.BOTH, expand=tk.YES)
text_area.bind('<KeyRelease>', runinbackground)
text_area.bind('<Button-1>', runinbackground)
runinbackground()
update_line_number()

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save", command=save_file2)
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

root.bind_all('<Control-n>', new_file)
root.bind_all('<Control-o>', open_file)
root.bind_all('<Control-s>', save_file)
root.bind_all('<Control-S>', save_as)

text_area.bind('<Control-x>', cut_text)
text_area.bind('<Control-c>', copy_text)
text_area.bind('<Control-v>', paste_text)
text_area.bind('<Control-a>', select_all_text)
text_area.bind('<Control-z>', undo)
text_area.bind('<Control-y>', redo)

text_area.bind('<Control-equal>', increase_font_size)
text_area.bind('<Control-minus>', decrease_font_size)

write_prefs()
root.mainloop()
