import os
import sys
import subprocess
import threading
from common import *

class nw():
    def macOS(openFile=""):
        global folder_path
        if platform.system() == "Darwin":
            run_path = os.path.realpath(__file__)
            cwd = os.getcwd()
            freeze_time = 1
            emptyString = ""
            with open(os.path.join(cache_path, "loadPreviousSave.lock"), "w", encoding='utf-8') as file:
                file.write(emptyString)
            subprocess.call(["/bin/rm", "-rf", folder_path])
            printlog("Launching new instance...")
            if openFile:
                subprocess.call(["/usr/bin/open", "-n", "-a", cwd + "/Notepad==.app", openFile])
            else:
                subprocess.call(["/usr/bin/open", "-n", "-a", cwd + "/Notepad==.app"])
            while os.path.exists(os.path.join(cache_path, "loadPreviousSave.lock")):
                pass
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

            emptyString = ""
            with open(os.path.join(cache_path, "loadPreviousSave.lock"), "w", encoding='utf-8') as file:
                file.write(emptyString)
            subprocess.call(["/bin/rm", "-rf", folder_path])
            printlog("Launching new instance...")
            def launcher():
                if os.path.exists(pyInstFile):
                    printlog("We are running in PyInstaller mode, running only the executable...")
                    subprocess.Popen([pyexe], preexec_fn=os.setsid, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
                else:
                    printlog("We are probably running in standard interpreted mode, launching executable with python file...")
                    subprocess.Popen([pyexe, run_path], preexec_fn=os.setsid, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
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
            while os.path.exists(os.path.join(cache_path, "loadPreviousSave.lock")):
                pass
            write_prefs()
            printlog("done")
        if platform.system() == "Linux":
            main()
        else:
            raise platformError("This function is only designed to be run on Linux. We do not understand why you would want this function to run anyway, nor how you got it to run. The function needs to be specific to the platform.")
