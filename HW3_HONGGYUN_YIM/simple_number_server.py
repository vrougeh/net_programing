from socket import *
import math

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 4444))
s.listen(5)
print('waiting...')

while True:
    c, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = c.recv(1024)
        if not data:
            break
        try:
            data = data.decode()
            if data.find("+") != -1:
                data = data.split('+')
                val = str(float(data[0]) + float(data[1]))
                
            elif data.find("-") != -1:
                data = data.split('-')
                val = str(float(data[0]) - float(data[1]))
            
            elif data.find("*") != -1:
                data = data.split('*')
                val = str(float(data[0]) * float(data[1]))
            
            elif data.find("/") != -1:
                data = data.split('/')
                val = str(float(data[0]) / float(data[1]))
            
        except:
            c.send(b'Try again')
        else:
            c.send(val.encode())

c.close()