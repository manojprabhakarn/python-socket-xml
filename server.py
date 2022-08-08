#! /usr/bin/python3

import socket as s
from urllib import response
import sys
from bs4 import BeautifulSoup

HOST = "127.0.0.1"
PORT = 1111

# socket
sck = s.socket(s.AF_INET,s.SOCK_STREAM)

sck.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,1)

# bind
sck.bind((HOST,PORT))

# listen
sck.listen()
print("Waiting for a connection...")

# Accept
conn, addr = sck.accept()
print("Connection received form {}:{}".format(addr[0],addr[1]))

# send to client
conn.send("Thank you for connecting, and your IP Address:{}\n".format(addr).encode())


print("Waiting for an incoming message")
data = conn.recv(1024)
msgforclient=data.decode()
detail="length of client data:{},size of the data is:{}\n".format(len(msgforclient),sys.getsizeof(msgforclient))

# xml tags
tagdetail=[]
soup=BeautifulSoup(msgforclient,"xml")
for child in soup.recursiveChildGenerator():
  if child.name:
    tagdetail.append(child.name)
listToStr = ' '.join(map(str, tagdetail))
print(listToStr)
  


print(detail)

conn.send(detail.encode())
conn.send(listToStr.encode())



while data:
    print(msgforclient,end="")
    data = conn.recv(1024)
    
 