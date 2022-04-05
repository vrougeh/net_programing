from socket import *

s = socket()
s.bind (('', 80))
s.listen(10)

while True:
    client, address = s.accept()

    data = client.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    req = req[0].split(' ')
    req = req[1].split('/')
    req = req[1]

    if req == 'index.html':
        f = open("index.html", 'r', encoding='utf-8')
        mimetype = 'text/html' 
        client.send(b'HTTP/1.1 200 OK\r\n')
        client.send(b'Content-Type: ' + mimetype.encode() + b'\r\n')
        client.send(b'\r\n')
        data = f.read()
        client.send(data.encode('euc-kr'))
    elif req == 'iot.png':
        f = open('iot.png', 'rb')
        mimetype = 'image/png'
        client.send(b'HTTP/1.1 200 OK\r\n')
        client.send(b'Content-Type: ' + mimetype.encode() + b'\r\n')
        client.send(b'\r\n')
        data = f.read()
        client.send(data)
    elif req == 'favicon.ico':
        f = open('favicon.ico', 'rb')
        mimetype = 'image/x-icon'
        client.send(b'HTTP/1.1 200 OK\r\n')
        client.send(b'Content-Type: ' + mimetype.encode() + b'\r\n')
        client.send(b'\r\n') 
        data = f.read()
        client.send(data)
    else:
        client.send(b'HTTP/1.1 404 Not Found\r\n')
        client.send(b'\r\n')
        client.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        client.send(b'<BODY>Not Found</BODY></HTML>')
    
    client.close()