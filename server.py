import socket 

ip = "127.0.0.1"
port = 8080

s = socket.socket()
s.bind((ip,port))
s.listen(2)
con,add = s.accept()
print("connection establish from",add)
a="connected"
con.send(a.encode())
while True:
    z = con.recv(1024)
    print(z.decode("utf-8"))
    w=input("msg>> ")
    con.send(w.encode("utf-8"))