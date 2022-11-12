import socket
import sys
import time

s = socket.socket()
host = socket.gethostname()
print(host)
port = 8080
s.bind((host, port))
s.listen(5)
conn, addr = s.accept()
print(addr, "has been connected")




