'''
Youtube Channel : Asim Security
Python Port Scanner
https://youtu.be/S6b686ZRyQ0
'''
import socket
from termcolor import colored
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input("[*] Please enter a Host to Scan: ")
def scan_port(port):
    if sock.connect_ex((host,port)):
        print(colored("[-] Port %d is closed" % (port),'red'))
    else:
        print(colored("[+] Port %d is open" % (port),'green'))

for port in range(1,1000):
    scan_port(port)
