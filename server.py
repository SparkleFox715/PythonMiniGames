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
GM = game(player("Player1", 1), player("Player2",2))
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
                    # for c in allclients:
                    #     try:
                    # allclients[0].sendall(pickle.dumps(GM))
                    # allclients[1].sendall(pickle.dumps(GM))
                    conn.sendall(pickle.dumps(GM))
                        # except:
                        #     continue
                elif data == "Begin":
                    GM.setState("GamesMenu")
                elif data =="TicTacToe":
                    GM.setState("TicTacToe")
                    GM.startTicTacToe()
                elif data.__contains__("place"):
                    p = int(data.split(" ")[1])
                    row = int(data.split(" ")[2])
                    col = int(data.split(" ")[3])
                    possible = GM.tic.place(row, col, p)
                    conn.sendall(pickle.dumps(possible))
                elif data.__contains__("P1"):
                    GM.player1 = player(data.split(" ")[1] ,1)
                elif data.__contains__("P2"):
                    GM.player2 = player(data.split(" ")[1],2)
                elif data == "Inc1":
                    GM.player1.score+=1
                elif data == "Inc2":
                    GM.player2.score+=1



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