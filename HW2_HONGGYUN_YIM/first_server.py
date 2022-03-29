import socket
s = socket.socket(socket.AF_INET, 
socket.SOCK_STREAM)
s.bind(('', 19000))
s.listen(2)
while True:
    client, addr = s.accept() 
    print('Connection from ', addr) #연결확인
    client.send(b'Hello ' + addr[0].encode())

    # 학생의 이름을 수신한 후 출력
    msg = client.recv(1024)
    print(msg.decode())


    #본인학번전송
    client.send((20171497).to_bytes(4,'big'))
    
    client.close()