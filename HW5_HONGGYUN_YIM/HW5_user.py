from socket import *
from tkinter.ttk import setup_master
import time
device1 = socket(AF_INET, SOCK_STREAM)
device2 = socket(AF_INET, SOCK_STREAM)
socket1 = 2017
socket2 = 1497
device1.connect(('localhost', socket1))
device2.connect(('localhost', socket2))
f = open('data.txt', 'a+')

while True:

    massage = input('Select device.\n')
    if massage == 'quit':
        device1.send('quit'.encode())
        device2.send('quit'.encode())
        break

    elif massage == '1':
        device1.send('Request'.encode())
        rsp = device1.recv(1024).decode()
        t = time.asctime()
        f.write(f'{t}: Device1: {rsp}\n')
        
               
    elif massage == '2':        
        device2.send('Request'.encode())
        rsp  = device2.recv(1024).decode()
        t = time.asctime()
        f.write(f'{t}: Device2: {rsp}\n')
        
    else:
        print(error)
        
        
device1.close()
device2.close()
f.close()