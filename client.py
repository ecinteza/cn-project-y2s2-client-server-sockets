import socket
import random
from datetime import datetime
from colorama import Fore, init

init()

colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTMAGENTA_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.YELLOW]

client_color = random.choice(colors)
ip = 'localhost'
port = 5002

s = socket.socket()
print(f"{Fore.LIGHTGREEN_EX}[*]Socket has been instantiated.{Fore.RESET}")

print(f"{Fore.LIGHTGREEN_EX}[*] Connecting to {ip}:{port}...{Fore.RESET}")
try:
    s.connect((ip, port))
    print(f"{Fore.LIGHTGREEN_EX}[+] Connected.{Fore.RESET}")
except:
    pass

print(f"{Fore.LIGHTRED_EX}Input 'quit' for exiting.{Fore.RESET}\n")

up = s.getsockname()[1]

addr = socket.gethostbyname(socket.gethostname())
while True:
    to_send = input()
    if to_send.lower() == 'quit':
        break
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M') 
    to_send = f"{client_color}[{date_now}] ({ip}) {addr}:{up} > {to_send}{Fore.RESET}"
    s.send(to_send.encode())

s.close()