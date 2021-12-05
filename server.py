import socket
from _thread import *
import sys
import threading
server = socket.gethostbyname(socket.gethostname())
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
allclients = []
lock = threading.Lock()
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


def threaded_client(conn, Stri):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            
            if data:
                print("Received: ", reply)
                print("Sending : ", reply)
                if not reply == "":
                    if reply.__contains__("P1"):
                        print("1111111")
                    elif reply.__contains__("P2"):
                        print("22222")
            print(len(allclients))
            with lock:
                for c in allclients:

                    c.sendall(str.encode(reply))
                if len(allclients)>1:
                    allclients[1].sendall(str.encode(reply))
        except error as e:
            print("failed"+str(e))
            break

    print("Lost connection")
    conn.close()

while True:
    print(1)
    conn, addr = s.accept()
    with lock:
        allclients.append(conn)
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, allclients))