from socket import *
from collections import defaultdict

port = 3333
BUFFSIZE = 1024
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

dictionary = defaultdict(list)

while True:
    data, address = sock.recvfrom(BUFFSIZE)
    data = data.decode()
    if data == 'quit':
        print("exit")
        break
    else:
        check = data.split(' ')
        print(data)
        if check[0] == 'send':
            massage = ' '.join(check[2:])
            dictionary[check[1]].append(massage)
            print(dictionary)
            sock.sendto("OK".encode(), address)
        elif check[0] == 'receive':
            print(dictionary)
            if check[1] in dictionary:
                if not dictionary[check[1]]:
                    print("notthing")
                    sock.sendto("No messages".encode(), address)
                else:
                    mail = dictionary[check[1]].pop(0)
                    print(dictionary)
                    sock.sendto(mail.encode(), address)
            else:
                sock.sendto("No messages".encode(), address)