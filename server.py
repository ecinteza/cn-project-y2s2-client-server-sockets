import socket
from threading import Thread
from colorama import Fore, init
import sys

init()

ip = 'localhost'
port = 5002

client_sockets = set()
print(f"{Fore.LIGHTGREEN_EX}[*]Socket has been instantiated.{Fore.RESET}")
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print(f"{Fore.LIGHTGREEN_EX}[*]Socket has been binded.{Fore.RESET}")
s.bind((ip, port))
s.listen(7)
addr = socket.gethostbyname(socket.gethostname())
print(f"{Fore.LIGHTGREEN_EX}[*] Listening as ({ip}) {addr}:{port}{Fore.RESET}")

def listen(c):
    while True:
        try:
            msg = c.recv(1024).decode()
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Fore.RESET}")
            client_sockets.remove(c)
            return
        
        if msg.split(" > ")[1].startswith('quit'):
            client_sockets.remove(c)
            return
        
        print(msg)

while True:
    (clisock, cliip) = s.accept()
    welcome = f"{Fore.LIGHTGREEN_EX}[+] {cliip} connected. Welcome!{Fore.RESET}"
    print(welcome)
    client_sockets.add(clisock)
    
    if len(client_sockets)==0:
        break
    
    t = Thread(target=listen, args=(clisock,))
    t.daemon = True
    t.start()
    
for sock in client_sockets:
    client_sockets.remove(sock)
    
sys.exit()