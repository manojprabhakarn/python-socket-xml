import socket
HOST = "127.0.0.1"
PORT = 1111

s = socket.socket()
s.connect((HOST,PORT))

xmldata = '''<?xml version="1.0" encoding="utf-8"?>
<bookstore>
  <book category="COOKING">
    <title lang="en">Everyday I8888talian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
  </book>
</bookstore>'''

s.sendall(xmldata.encode())

while True: 
    msg = s.recv(1024)
    if len(msg) <=0:
        break
    print(msg.decode())

