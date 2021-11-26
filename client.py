import socket

ip = "127.0.0.1"
port = 8080

s = socket.socket()
s.connect((ip,port))

c = s.recv(1024)
print(c.decode("utf-8"))
    
while True:
    a = input("msg>> ")
    s.send(a.encode('utf-8'))
    c = s.recv(1024)
    print(c.decode("utf-8"))
