import socket
import _thread
import sys

server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)


s.listen(2)#number of people in netword
print("Waiting for connection, Server started")

def threaded_client(conn):
    pass

while True:
    