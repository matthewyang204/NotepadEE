import main
import platform

# To trigger PyInstaller
if platform.system() != "Darwin":
    import os
    import sys
    import hashlib
    import builtins
    import tempfile
    import re
    import pathlib
    import traceback
    import errno
    import platform
    import subprocess
    import threading
    import signal
    import shutil
    from pathlib import Path
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import filedialog
    from tkinter import font
    import idlelib.colorizer
    import idlelib.percolator
    import pyperclip
    import tkinter
    import tklinenums
    from spellchecker import SpellChecker

if __name__ == "__main__":
    main.main()
