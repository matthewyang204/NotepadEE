import tkinter as tk
from tkinter import messagebox, font, filedialog
import os
import sys
import platform


versionInfo = """Notepad==, version 5.0.8
(C) 2024-2025, Matthew Yang"""

helpInfo = f"""{versionInfo}

Usage: "notepad==" [OPTIONS] [<filepath>]

Options:
--version, -v     Display version info and exit
--help, -h        Display this help message and exit

Note that [<filepath>] is not required and if not given, the file that was previously opened will be opened in the new instance.
"""


arg = sys.argv
if len(arg) <= 1:
    pass
else:
    if arg[1] == '--version' or arg[1] == '-v':
        print(versionInfo)
        sys.exit()
    elif arg[1] == '--help' or arg[1] == '-h':
        print(helpInfo)
        sys.exit()

# define the variables required for the program to start
local_app_data_path = os.getenv('LOCALAPPDATA')

# for debugging on Linux
# local_app_data_path = os.path.expanduser('~')

filearg = sys.argv
global openFile
global fileToBeOpened
if len(filearg) <= 1:
    openFile = 0
    print("No arguments provided. Proceeding to load program with last known file...")
else:
    openFile = 1
    print("Assuming argument is the file to open. Loading file...")
    fileToBeOpened = filearg[1]

global file_open
file_open = 0
last_file_path = os.path.join(local_app_data_path, 'NotepadEE', 'prefs',
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

global folder_path
folder_path = os.path.join(local_app_data_path, 'NotepadEE', 'prefs')
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

global last_write
last_write = os.path.join(local_app_data_path, 'NotepadEE', 'prefs', 'last_write')
if not os.path.exists(last_write):
    with open(last_write, 'w'):
        pass


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# useful to avoid overwhelming user when he/she hits File > New
global file_written
file_written = 0
print("file_written set to " + str(file_written))

# load the GUI before defining userland functions
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

file_var = tk.StringVar()
file_label = tk.Label(status_frame, textvariable=file_var)
file_label.pack(side=tk.LEFT)

# define the userland functions
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

def debug_var(event=None):
    global file_open, current_file
    if current_file:
        print("Current file variable works")
        print(current_file)
    else:
        print("Not intact")
    if file_open:
        print("File_open variable is intact")
        print(file_open)
    else:
        print("Not working")
    return 'break'

def autosave_file(event=None):
    global current_file
    global file_open
    # if a file is open, save to the save PATH, otherwise, quit upon known error
    try:
        if file_open == 1:
            with open(current_file, 'w') as file:
                text = text_area.get('1.0', 'end-1c')
                file.write(text)
    except FileNotFoundError:
        return 'break'
    print("Autosaved file")


def write_prefs(event=None):
    global current_file, file_open
    with open(
            os.path.join(local_app_data_path, 'NotepadEE', 'prefs','last_write'), 'w') as file:
        file.write(text_area.get('1.0', 'end-1c'))
    last_file_path = os.path.join(local_app_data_path, 'NotepadEE', 'prefs', 'last_file_path')
    with open(last_file_path, 'w') as file:
        file.write(str(current_file))
    autosave_file()
    print("Prefs written")

# save_as provides the dialog
def save_as(event=None):
    global current_file, file_open
    file_path = filedialog.asksaveasfilename(
        defaultextension="",
        filetypes=(
            ("All Files (*.*)", "*.*"),

            # Notepad files
            ("Plain text file (.txt)", ".txt"),
            ("Log file (.log)", ".log"),

            # ms ini/inf
            ("INI file (.ini)", ".ini"),
            ("INF file (.inf)", ".inf"),

            # C, C++, objc
            ("C, C++, objc header (.h)", ".h"),
            ("C, C++, objc header (.hh)", ".hh"),
            ("C, C++, objc header (.hpp)", ".hpp"),
            ("C, C++, objc header (.hxx)", ".hxx"),
            ("C, C++, objc source (.c)", ".c"),
            ("C, C++, objc source (.cpp)", ".cpp"),
            ("C, C++, objc source (.cxx)", ".cxx"),
            ("C, C++, objc source (.cc)", ".cc"),
            ("C, C++, objc source (.m)", ".m"),
            ("C, C++, objc source (.mm)", ".mm"),
            ("C, C++, objc project (.vcxproj)", ".vcxproj"),
            ("C, C++, objc project (.vcproj)", ".vcproj"),
            ("C, C++, objc properties (.props)", ".props"),
            ("C, C++, objc properties (.vsprops)", ".vsprops"),
            ("C, C++, objc manifest (.manifest)", ".manifest"),

            # Java, C#, Pascal
            ("Java file (.java)", ".java"),
            ("Pascal file (.pas)", ".pas"),
            ("Pascal file (.pp)", ".pp"),
            ("Include file (.inc)", ".inc"),

            # .NET code
            ("Visual Basic (.vb)", ".vb"),
            ("Visual Basic script (.vbs)", ".vbs"),
            ("C# file (.cs)", ".cs"),

            # Web script files
            ("HTML file (.html)", ".html"),
            ("HTML file (.htm)", ".htm"),
            ("Server-side HTML (.shtml)", ".shtml"),
            ("Server-side HTML (.shtm)", ".shtm"),
            ("HTML Application (.hta)", ".hta"),
            ("ASP file (.asp)", ".asp"),
            ("ASP.NET file (.aspx)", ".aspx"),
            ("CSS file (.css)", ".css"),
            ("JavaScript file (.js)", ".js"),
            ("JSON file (.json)", ".json"),
            ("JavaScript module (.mjs)", ".mjs"),
            ("JavaScript module (.jsm)", ".jsm"),
            ("JSP file (.jsp)", ".jsp"),
            ("PHP file (.php)", ".php"),
            ("PHP3 file (.php3)", ".php3"),
            ("PHP4 file (.php4)", ".php4"),
            ("PHP5 file (.php5)", ".php5"),
            ("PHP script (.phps)", ".phps"),
            ("PHP script (.phpt)", ".phpt"),
            ("PHP file (.phtml)", ".phtml"),
            ("XML file (.xml)", ".xml"),
            ("XHTML file (.xhtml)", ".xhtml"),
            ("XHTML file (.xht)", ".xht"),
            ("XUL file (.xul)", ".xul"),
            ("KML file (.kml)", ".kml"),
            ("XAML file (.xaml)", ".xaml"),
            ("XSML file (.xsml)", ".xsml"),

            # Script files
            ("Shell script (.sh)", ".sh"),
            ("Bash script (.bsh)", ".bsh"),
            ("Bash script (.bash)", ".bash"),
            ("Batch file (.bat)", ".bat"),
            ("Command file (.cmd)", ".cmd"),
            ("NSIS script (.nsi)", ".nsi"),
            ("NSIS header (.nsh)", ".nsh"),
            ("Lua script (.lua)", ".lua"),
            ("Perl script (.pl)", ".pl"),
            ("Perl module (.pm)", ".pm"),
            ("Python script (.py)", ".py"),
            ("Inno Setup script (.iss)", ".iss"),
            ("Makefile", ".mak"),

            # Property scripts
            ("Resource file (.rc)", ".rc"),
            ("ActionScript (.as)", ".as"),
            ("MaxScript (.mx)", ".mx"),

            # Fortran, TeX, SQL
            ("Fortran file (.f)", ".f"),
            ("Fortran file (.for)", ".for"),
            ("Fortran 90 file (.f90)", ".f90"),
            ("Fortran 95 file (.f95)", ".f95"),
            ("Fortran 2000 file (.f2k)", ".f2k"),
            ("TeX file (.tex)", ".tex"),
            ("SQL file (.sql)", ".sql"),

            # Miscellaneous files
            ("NFO file (.nfo)", ".nfo")))
    current_file = file_path
    # if file_path doesn't exist, let's stop the function and return False
    if not file_path:
        return False
    
    # if we get a valid file_path, let's save via dialog
    try:
        print("Saving file to location:")
        print(file_path)
        with open(file_path, 'w') as file:
            text = text_area.get(1.0, "end-1c")
            file.write(text)
        write_prefs()
        file_open = 1
        print("File was saved to different location successfully.")
        return True
    
    # if any errors manage to get past this, let's do an exception to quit gracefully
    except FileNotFoundError:
        messagebox.showerror("Error", "Location nonexistent")
        return False

def save_file(warn):
    global current_file, file_open, file_written
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
                    print("File saved without warning")
                    return True
            else:
                return True
        elif warn == "w":
            if platform.system() == "Darwin":
                pass
            else:
                if file_written == 1:
                    response = messagebox.askyesno("Warning: File is not saved","The current file is not saved. Changes may be lost if they are not saved. Do you want to save before exiting?")
                    if response:
                        if save_as():
                            print("File saved")
                            return True
                    else:
                        return True
        else:
            response = messagebox.askyesno("Create new file","The file does not exist. Do you want to create it as a new file?")
            if response:
                if save_as():
                    print("File saved after warning user")
                    return True
            else:
                return True

def save_file2(event=None):
    global current_file, file_open
    print("No-warning wrapper triggered, running save_file with nowarning option")
    save_file("n")

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
        print("File opened successfully.")
    write_prefs()

def new_file(event=None):
    global current_file, file_open, file_written

    # Check if there is text in text_area
    if file_written == 1:
        # Only run this code if save_file, otherwise, don't force user to clear
        if save_file("y"):
            text_area.delete(1.0, "end")
            print("Cleared text_area")
            current_file = ""
            write_prefs()
            file_open = 0
            print("New file created")
            file_written = 0
    
    # Otherwise, clear without obstruction
    else:
        text_area.delete(1.0, "end")
        print("Cleared text_area")
        current_file = ""
        write_prefs()
        file_open = 0
        print("New file created")


def cut_text(event=None):
    text_area.clipboard_clear()
    text_area.clipboard_append(text_area.get("sel.first", "sel.last"))
    text_area.delete("sel.first", "sel.last")
    print("Cut option ran successfully")
    return 'break'


def copy_text(event=None):
    text_area.clipboard_clear()
    text_area.clipboard_append(text_area.get("sel.first", "sel.last"))
    print("Text copied to clipboard successfully")
    return 'break'


def paste_text(event=None):
    text_area.insert("insert", text_area.clipboard_get())
    print("Text pasted from clipboard successfully")
    return 'break'


def select_all_text(event=None):
    text_area.tag_add("sel", "1.0", "end")
    print("All text selected")
    return 'break'


def undo(event=None):
    try:
        text_area.edit_undo()
    except tk.TclError:
        pass
    print("Edit undone")


def redo(event=None):
    try:
        text_area.edit_redo()
    except tk.TclError:
        pass
    print("Edit redone")

def find_and_replace(event=None):
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
        text_area.mark_set("insert", f"{line_number}.0")

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
        print("invalidArg")
        return "invalidArg"

def findNext(text):
    try:
        last_highlight = text_area.index("highlight.last")
        start = last_highlight
    except tk.TclError:
        cPos_line, cpos_column = cPos("both")
        start = f"{cPos_line}.{cpos_column}"
        # start= "1.0"

    text_area.tag_remove("highlight", "1.0", "end")
    try:
        start = text_area.search(text, start, stopindex="end")
        end = f"{start} + {len(text)}c"
        text_area.tag_add("highlight", start, end)
    except Exception as e:
        start = "1.0"
        start = text_area.search(text, start, stopindex="end")
        end = f"{start} + {len(text)}c"
        text_area.tag_add("highlight", start, end)
    
    text_area.tag_config("highlight", background="yellow")

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
    
    find_button = tk.Button(popup, text="Find", command = findNext_wrapper)
    close_button = tk.Button(popup, text="Close", command=close)
    clear_button = tk.Button(popup, text="Clear", command=clear)
    find_button.pack()
    clear_button.pack()
    close_button.pack()
    entrybox.bind('<Return>', findNext_wrapper)

def mark_text(event=None):
    selectStart = text_area.index("sel.first")
    selectEnd = text_area.index("sel.last")
    print(f"Current selection is {selectStart}, {selectEnd}")
    print("Clearing all current highlights in selection...")
    text_area.tag_remove("highlight_permanent", selectStart, selectEnd)
    print("Configuring highlight_permanent tags to selection...")
    text_area.tag_add("highlight_permanent", selectStart, selectEnd)
    print("Configuring tagged text to highlight...")
    text_area.tag_config("highlight_permanent", background="green")
    print("done")
    
def unmark_text(event=None):
    selectStart = text_area.index("sel.first")
    selectEnd = text_area.index("sel.last")
    print(f"Current selection is {selectStart}, {selectEnd}")
    print("Clearing all current highlights in selection...")
    text_area.tag_remove("highlight_permanent", selectStart, selectEnd)
    print("done")

def unmark_all_text(event=None):
    print("Clearing all current highlights...")
    text_area.tag_remove("highlight_permanent", "1.0", "end")
    print("done")

def update_line_number(event=None):
    line, column = text_area.index(tk.INSERT).split('.')
    line_var.set("Line: " + line)
    column_var.set("Column: " + column)
    words = text_area.get(1.0, 'end-1c').split()
    word_count_var.set("Words: " + str(len(words)))
    file_var.set("File: " + os.path.basename(current_file))
    if current_file:
        root.title(f"Notepad== - {current_file}")
    else:
        root.title("Notepad==")
    # print("Status bar updated")
    root.after(100, update_line_number)


def increase_font_size(event=None):
    current_size = text_font['size']
    text_font.config(size=current_size + 1)
    print("Font size increased by 1 pt")


def decrease_font_size(event=None):
    current_size = text_font['size']
    text_font.config(size=current_size - 1)
    print("Font size decreased by 1 pt")

# Create a function to check for text in text_area
def check_file_written(event=None):
    global file_written
    print("Checking if text_area has been edited by the user to contain text...")
    current_text = text_area.get(1.0, "end-1c").strip()

    # if there is text, set it to 1
    if current_text:
        print("There is text; setting to 1")
        file_written = 1

    # otherwise, set it to 0
    else:
        print("No text")
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
        #print("Current file path: " + current_file)
        #print("File open: " + str(file_open))
        print("File loaded")
    else:
        text_area.delete(1.0, "end")
        with open(file_path, 'w') as file:
            text = text_area.get(1.0, "end-1c")
            file.write(text)
        file_open = 1
        current_file = os.path.abspath(file_path)
        #print("Current file path: " + current_file)
        #print("File open: " + str(file_open))
        write_prefs()
        print("Because the file doesn't exist, it was created as a blank new file instead")

def exit_handler(event=None):
    print("Telling user to save file before exit...")
    save_file("w")
    print("Exiting...")
    sys.exit()

if openFile == 1:
    runonfilearg(fileToBeOpened)
else:
    print("Program loaded")

text_area.pack(fill=tk.BOTH, expand=tk.YES)
text_area.bind('<KeyRelease>', runinbackground)
text_area.bind('<Button-1>', runinbackground)
runinbackground()
update_line_number()

check_file_written()

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
if platform.system() == "Darwin":
    text_area.bind('<Command-Z>', redo)
else:
    text_area.bind('<Control-y>', redo)
text_area.bind('<Control-m>', mark_text)
text_area.bind('<Control-M>', unmark_text)
text_area.bind('<Control-U>', unmark_all_text)
text_area.bind('<Control-f>', find_text)
text_area.bind('<Control-R>', find_and_replace)
text_area.bind('<Control-G>', go_to_line)

text_area.bind('<Control-equal>', increase_font_size)
text_area.bind('<Control-minus>', decrease_font_size)

root.protocol('WM_DELETE_WINDOW', exit_handler)

write_prefs()
root.mainloop()
