# -*- coding: euc-kr -*-
from socket import *
from random import randint

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 2017))
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
            temp = randint(0, 40)
            humid = randint(0, 100)
            lilum = randint(70, 150)
            totaldata = f"Temp={temp}, Humid={humid}, lilum={lilum}"
            print(totaldata)
            client.send(totaldata.encode())
        elif data == 'quit':
            break
    if data == 'quit':
        break

    client.close()