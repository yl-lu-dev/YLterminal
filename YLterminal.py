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


print('YLterminal version: update 1.8')
print('made on: 2025-07-26')
print('finish time: 2025-07-31') 
print('publish time: 2025-07-31')
print('''update 1.8 started on: 2025-07-31
update finished on: 2025-07-32
update released on: 2025-08-02
''')

os.system("color 7")

while True:

    enter = input(f"{yellow}$ {notRED}").strip().lower()

    if enter == "help":
        print('''
    
    mkd - creats a new dir
    network /show - shows the password for a wifi you have connected to 
    pw - pings a website
    excute /bypass: admin - bypasses the uac when runing a file
    tmp /rm - deletes all temp files on your computer
    here - shows the current  path you are in
    list - shows all files in the dir
    c - changes dir
    dir /del - removes dir
    port /scan - port scanner 
    echo /status - tells if echo is on or off
    list /all - show every file in the computer
    file /creat - creats a file
    filerun - runs a file in your courrent dir 
        ''')
    
    elif enter == "list":
        os.system("DIR")

    elif enter == "c":

        dir = input("dir:")

        try:
            os.chdir(dir)

            here2 = dirk()

            print(f"Changed to: {os.getcwd()}")

        except FileNotFoundError:
            print(f"{RED}No such dir{notRED}")
        except NotADirectoryError:
            print(f"{RED}No such dir{notRED}")

 
    
    elif enter == "here":
        dirk()

    elif enter == "list /all":
        os.chdir(r"c:\\")
        os.system("dir /s")

    elif enter == "tmp /rm":
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
    
    elif enter == "filerun":
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
     
    elif enter == "excute /bypass: admin":
        filetoby = input("file: ")

        cmd = f"set __compat_layer=runasinvoker & {filetoby}"

        os.system(cmd)

    elif enter == "pw":
        web = input("ip/website: ")
        data = int(input("how many bytes?(1-65000): "))
  
        if data > 65000:
            print("size is to large")

        else :
            ping = f"ping {web} -l {data}"
            os.system(ping)

    elif enter == "network /show":
        wifi = input("wifi name: ")

        wific = f'netsh wlan show profile name="{wifi}" key=clear'
        
        result = subprocess.run(wific, shell=True, capture_output=True, text=True)
        wifi_n = result.stdout.strip()

        if wifi_n == f'Profile "{wifi}" is not found on the system.':
            print(f"{RED}You have not conected to the network: {wifi}{notRED}")

        else:
            print(wifi_n)
    
    elif enter == "mkd":
        dir = input("DIR name: ")
        os.mkdir(dir)
    


    else:
        print(f"{RED}unrecognized command type help to see the list of availible cammands{notRED}")
    

