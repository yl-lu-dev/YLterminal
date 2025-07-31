import socket
import subprocess
import os
import shutil
import time


os.system("title YLterminal") 
    
def pause():
    time.sleep(2)   

def dirk():
    c = os.getcwd()    
    print(c)
    
yellow = "\033[33m"  
 
green = "\033[32m"

RED = "\033[31m"

notRED = "\033[0m"


print('YLterminal version: release 1.0')
print('made on: 2025-07-26')
print('finish time:') 
print('publish time:')
     

os.system("color 7")

while True:

    enter = input(f"{yellow}$ {notRED}").strip().lower()

    if enter == "help":
        print('''
    tmp /remove - deletes all temp files on your computer
    show /dir - shows the current  path you are in
    dir /show - shows all files in the dir
    dir /change - changes dir
    dir /show /del - removes dir
    port /scan - port scanner 
    echo /status - tells if echo is on or off
    dir /show /all - show every file in the computer
    file /creat - creats a file
    dir /excute - runs a file in your courrent dir 
        ''')
    
    elif enter == "dir /show":
        os.system("DIR")

    elif enter == "dir /change":
        a = input("enter the dir path: ")
        os.chdir(a)
        dirk()
        print("your current dir path is ^")
    
    elif enter == "show /dir":
        dirk()

    elif enter == "dir /show /all":
        os.chdir(r"c:\\")
        os.system("dir /s")

    elif enter == "tmp /remove":
        os.chdir(r"c:\\")
        print("deleting temp files...")
        os.system("del /s /q *.tmp")    
    
    elif enter == "dir /show /del":
        path = input("enter dir path:")
        if path == r"c:\windows\system32":
            print("unsafe removal")
        
        
        else:
            print(f"deleting{path}")
            pause()
            shutil.rmtree(path)
            print(f"{path} is seccesfully deleted!")
    
    elif enter == "dir /excute":
        file = input("file:")
        os.startfile(file)
    
    elif enter == "file /creat":
        
        file = input("File name:")
        ext = input("extension:")
        cont = input("content:")
        Full_name = f"{file}.{ext}"
        
        print("creating file...")
        
        with open(Full_name, 'w') as f:
            f.write(cont)
        print(f"finished! The file: {file}.{ext} is in: ")
        dirk()
    
    elif enter == "echo /status":
        
        result = subprocess.run("echo", shell=True, capture_output=True, text=True)
        
        echo = result.stdout.strip()
        
        if echo == "ECHO is on.":
            print(f"echo is {green}on{notRED}")
        
        elif echo == "ECHO is off.":
            print(f"echo is {RED}off{notRED}")
            
        else:
            print("something went wrong")  
    
    elif enter == "port /scan":
    
        ip = input("Enter IP to scan: ")
        start = int(input("Start port: "))
        end = int(input("End port: "))
        
        print(f"{yellow}scanning ports...{notRED}")

        found_open = False

        for port in range(start, end + 1):
           with socket.socket() as s:
                s.settimeout(0.5)
                if s.connect_ex((ip, port)) == 0:
                    print(f"Port {port} {green}open{notRED}")
                    found_open = True

        if not found_open:
            print(f"{RED}No open ports found in the range.{notRED}")
     
    
    
    else:
        print(f"{RED}unrecognized command press help to seee the list of availible cammands{notRED}")
    

