import os
import sys
import traceback
from tkinter import messagebox, filedialog
import errno
import common
import platform
import platformSpecific as ps
from exceptions import UnsupportedEncodingError

text_area = None

def retrieve_file(input):
    for enc in common.encodings[:]:
        try:
            with open(input, 'r', encoding=enc) as file:
                fileContent = file.read()
            return fileContent
        except UnicodeDecodeError:
            print("UnicodeDecodeError caught!")
            print("File is not " + str(enc) + ", trying next encoding...")
        except LookupError:
            print("LookupError caught!")
            print("Encoding not supported in this copy of Python, removing from list to avoid future clashes...")
            common.encodings.remove(enc)
    messagebox.showinfo("The program crashed due to an error", "The program has crashed due to an error. Please relaunch the program; any unsaved work will be recovered automatically on relaunch.")
    try:
        raise UnsupportedEncodingError("The file at " + str(input) + " could not be opened due to its encoding not being supported. The program has crashed itself to avoid further problems.")
    except UnsupportedEncodingError:
        traceback.print_exc()
        sys.exit(1)

def runonarg(arg):
    if os.path.exists(arg):
        content = retrieve_file(arg)
        if common.file_written == 1:
            if platform.system() == "Darwin":
                common.printlog("Calling platform launcher for macOS")
                ps.nw.macOS(openFile=arg)
            elif platform.system() == "Linux":
                common.printlog("Calling platform launcher for Linux")
                ps.nw.Linux(openFile=arg)
            else:
                text_area.delete(1.0, "end")
                common.current_file = arg
                text_area.insert(1.0, content)
                common.file_open = 1
        else:
            text_area.delete(1.0, "end")
            common.current_file = arg
            text_area.insert(1.0, content)
            common.file_open = 1
        common.printlog("File loaded, closing resource...", end='')
        print("done")
    else:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), arg)

def autosave_file(event=None):
    try:
        if common.file_open == 1:
            with open(common.current_file, 'w', encoding='utf-8') as file:
                text = text_area.get('1.0', 'end-1c')
                file.write(text)
    except FileNotFoundError:
        return 'break'
    common.printlog("Autosaved file")

def write_prefs(event=None):
    common.setup_prefs()
    with open(os.path.join(os.path.expanduser('~'), '.notepadee', 'prefs', 'last_write'), 'w', encoding='utf-8') as file:
        file.write(text_area.get('1.0', 'end-1c'))
    last_file_path = os.path.join(os.path.expanduser('~'), '.notepadee', 'prefs', 'last_file_path')
    with open(last_file_path, 'w', encoding='utf-8') as file:
        file.write(str(common.current_file))
    autosave_file()
    common.printlog("Wrote prefs successfully")

def save_as(event=None):
    file_path = filedialog.asksaveasfilename(
        defaultextension="",
        filetypes=(
            ("All Files", "*.*"),
            ("Plain text file", ".txt"),
            ("Log file", ".log"),
            ("INI file", ".ini"),
            ("INF file (.inf)", ".inf"),
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
            ("Java file", ".java"),
            ("Pascal file", ".pas"),
            ("Pascal file", ".pp"),
            ("Include file", ".inc"),
            ("Visual Basic (.vb)", ".vb"),
            ("Visual Basic script (.vbs)", ".vbs"),
            ("C# file (.cs)", ".cs"),
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
            ("Makefile", ".mak"),
            ("Resource file", ".rc"),
            ("ActionScript", ".as"),
            ("MaxScript", ".mx"),
            ("Fortran file", ".f"),
            ("Fortran file", ".for"),
            ("Fortran 90 file", ".f90"),
            ("Fortran 95 file", ".f95"),
            ("Fortran 2000 file", ".f2k"),
            ("TeX file", ".tex"),
            ("SQL file", ".sql"),
            ("NFO file", ".nfo")))
    common.current_file = file_path
    if not file_path:
        return False
    try:
        common.printlog("Saving file to location:")
        common.printlog(file_path)
        with open(file_path, 'w', encoding='utf-8') as file:
            text = text_area.get(1.0, "end-1c")
            file.write(text)
        write_prefs()
        common.file_open = 1
        common.printlog("File was saved to different location successfully.")
        return True
    except FileNotFoundError:
        messagebox.showerror("Error", "Location nonexistent")
        return False

def open_file_v2(event=None):
    common.file_written = common.file_written
    save_file("y")
    file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    if file_path:
        content = retrieve_file(file_path)
        if common.file_written == 1:
            if platform.system() == "Darwin":
                ps.nw.macOS(openFile=file_path)
            elif platform.system() == "Linux":
                ps.nw.Linux(openFile=file_path)
            else:
                text_area.delete(1.0, "end")
                common.current_file = file_path
                text_area.insert(1.0, content)
                common.file_open = 1
        else:
            text_area.delete(1.0, "end")
            common.current_file = file_path
            text_area.insert(1.0, content)
            common.file_open = 1
        common.printlog("New file opened")
        print("done")

def save_file(warn):
    if common.file_open == 1:
        try:
            with open(common.current_file, 'w', encoding='utf-8') as file:
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
                    common.printlog("File saved without warning")
                    return True
            else:
                return True
        elif warn == "w":
            if common.file_written == 1:
                response = messagebox.askyesnocancel("Warning: File is not saved","The current file is not saved. Changes may be lost if they are not saved. Do you want to save before exiting?")
                if response:
                    if save_as():
                        common.printlog("File saved")
                        return True
                elif response == None:
                    return False
                else:
                    return True
            else:
                return True
        else:
            response = messagebox.askyesno("Create new file","The file does not exist. Do you want to create it as a new file before proceeding?")
            if response:
                if save_as():
                    common.printlog("File saved after warning user")
                    return True
            else:
                return True

def save_file2(event=None):
    common.printlog("No-warning wrapper triggered, running save_file with nowarning option")
    save_file("n")

def new_file(event=None):
    if common.file_written == 1:
        if save_file("y"):
            text_area.delete(1.0, "end")
            common.printlog("Cleared text_area")
            common.current_file = ""
            write_prefs()
            common.file_open = 0
            common.printlog("New file created")
            common.file_written = 0
    else:
        text_area.delete(1.0, "end")
        common.printlog("Cleared text_area")
        common.current_file = ""
