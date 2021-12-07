import socket
from _thread import *
import sys
import threading
from Game import game
import pickle
from PlayerInfo import player
server = socket.gethostbyname(socket.gethostname())
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
allclients = []
GM = game(player("Player1"), player("Player2"))
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


def threaded_client(conn):
    conn.send(str.encode("Connected"))

    while True:
        try:
            data = conn.recv(2048).decode()
            if not data:
                break
            if data:
                # print("Received: ", reply)
                # print("Sending : ", reply)
                if data =="getGame":
                    for c in allclients:
                        try:
                            c.sendall(pickle.dumps(GM))
                        except:
                            continue
                elif data == "Begin":
                    GM.setState("GamesMenu")



        except error as e:
            print("failed"+str(e))
            break

    print("Lost connection")
    conn.close()

while True:
    conn, addr = s.accept()
    allclients.append(conn)
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn,))