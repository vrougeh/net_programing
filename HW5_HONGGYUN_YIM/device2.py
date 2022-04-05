# -*- coding: euc-kr -*-
from socket import *
from random import randint

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 1497))
s.listen(10)
print('Please wating..')

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        data = data.decode()
        print(data)
        if data == 'Request':
            heartbeat = randint(40,140)
            steps = randint(2000,6000)
            cal = randint(1000,4000)
            totaldata = f"Heartbeat={heartbeat}, Steps={steps}, Cal={cal}"
            print(totaldata)
            client.send(totaldata.encode())
        elif data == 'quit':
            break
    if data == 'quit':
        break

    client.close()