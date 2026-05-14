import os
import sys
import hashlib
import builtins
import tkinter as tk

# Define and create, if applicable, a cache folder
import tempfile
cache_path = os.path.join(os.path.expanduser('~'), '.notepadee', 'cache')
try:
    os.makedirs(cache_path, exist_ok=True)
except Exception:
    # Fallback: ignore failures to create cache (permissions may prevent it)
    pass

username = os.path.expanduser('~').encode()
unSHA256 = hashlib.sha256()
unSHA256.update(username)
unDigest = unSHA256.hexdigest()
# Use platform temporary directory instead of hard-coded '/tmp'
tmpdir = tempfile.gettempdir()
logDir = os.path.join(tmpdir, str(unDigest) + '-log')
try:
    os.makedirs(logDir, exist_ok=True)
except Exception:
    # Fallback: try creating log dir inside user cache
    try:
        logDir = os.path.join(cache_path, str(unDigest) + '-log')
        os.makedirs(logDir, exist_ok=True)
    except Exception:
        pass

# Open a log file in write mode
# log_file = os.path.join(cache_path, "notepadee_log.txt")
log_file = os.path.join(logDir, "notepadee_log.txt")

# Get current PID
pid = os.getpid()

# Special printlog statement to print stuff that doesn't belong in a console to the log file
def printlog(message, *args, **kwargs):
    # with open(log_file, 'a', encoding='utf-8') as file:
    #     file.write("Notepad== at " + str(pid) + ": " + str(message))
    print("Notepad== at " + str(pid) + ": " + str(message), *args, **kwargs)

versionInfo = """Notepad==, version 5.3.1
(C) 2024-2026 Matthew Yang"""

arg = sys.argv

encodings = [
    "ascii",
    "utf-8",
    "utf-16",
    "utf-32",
    "latin-1",
    "cp1252",
    "shift_jis",
    "euc_jp",
    "iso2022_jp",
    "gb2312",
    "gbk",
    "big5",
    "euc_kr",
    "cp1251",
    "koi8_r",
    "mac_roman",
    "cp437",
    "utf-8-sig",
    "utf-7",
    "iso8859_2",
    "iso8859_15",
    "cp850",
]

global fileToBeOpened
global openFile
fileToBeOpened = None
openFile = None

folder_path = os.path.join(os.path.expanduser('~'), '.notepadee', 'prefs')

global file_open
file_open = 0
last_file_path = os.path.join(os.path.expanduser('~'), '.notepadee', 'prefs', 'last_file_path')
if os.path.exists(last_file_path):
    with open(last_file_path, 'r', encoding='utf-8') as file:
        current_file = file.read()
        if current_file.strip() == '':
            file_open = 0
        else:
            file_open = 1
else:
    current_file = ""
    file_open = 0

global last_write
last_write = os.path.join(os.path.expanduser('~'), '.notepadee', 'prefs', 'last_write')

file_written = 0
printlog("file_written set to " + str(file_written))

def setup_prefs(event=None):
    global folder_path, last_file_path, last_write
    
    try:
        os.makedirs(folder_path, exist_ok=True)
    except Exception:
        pass

    # Ensure parent directory exists before touching files
    try:
        parent = os.path.dirname(last_file_path)
        os.makedirs(parent, exist_ok=True)
    except Exception:
        pass

    if not os.path.exists(last_file_path):
        with open(last_file_path, 'w', encoding='utf-8'):
            pass

    if not os.path.exists(last_write):
        with open(last_write, 'w', encoding='utf-8'):
            pass

def setup_logging():
    global log_file
    log_file = open(log_file, 'a', encoding='utf-8', buffering=1)
    sys.stdout = log_file
    sys.stderr = log_file
    original_print = builtins.print
    def flushed_print(*args, **kwargs):
        if 'flush' not in kwargs:
            kwargs['flush'] = True
        if 'end' not in kwargs:
            kwargs['end'] = '\n'
        return original_print(*args, **kwargs)
    builtins.print = flushed_print

setup_prefs()

class SimpleVar:
    def __init__(self, value=1):
        self._value = value
    def get(self):
        return self._value
    def set(self, v):
        self._value = v

# Provide a safe default for autosave_enabled (avoids creating a Tk root at import time)
autosave_enabled = SimpleVar(1)

        
