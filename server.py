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
                elif data == "DuelGame":
                    GM.setState("Duel")
                    GM.startDuelGame()
                elif data.__contains__("place"):
                    p = int(data.split(" ")[1])
                    row = int(data.split(" ")[2])
                    col = int(data.split(" ")[3])
                    possible = GM.tic.place(row, col, p)
                    conn.sendall(pickle.dumps(possible))
                elif data.__contains__("P1Username"):
                    GM.player1 = player(data.split(" ")[1] ,1)
                elif data.__contains__("P2Username"):
                    GM.player2 = player(data.split(" ")[1],2)
                elif data == "Inc1":
                    GM.player1.score+=1
                elif data == "Inc2":
                    GM.player2.score+=1
                elif data == "DuelP1 Left":
                    GM.du.moveLeft(1)
                elif data == "DuelP1 Right":
                    GM.du.moveRight(1)
                elif data == "DuelP1 Up":
                    GM.du.moveUp(1)
                elif data == "DuelP1 Down":
                    GM.du.moveDown(1)
                elif data == "DuelP2 Left":
                    GM.du.moveLeft(2)
                elif data == "DuelP2 Right":
                    GM.du.moveRight(2)
                elif data == "DuelP2 Up":
                    GM.du.moveUp(2)
                elif data == "DuelP2 Down":
                    GM.du.moveDown(2)
                elif data == "Time1":
                    GM.du.assignTime(1)
                elif data == "ResetTime1":
                    GM.du.resetTime(1)
                elif data == "Time2":
                    GM.du.assignTime(2)
                elif data == "ResetTime2":
                    GM.du.resetTime(2)
                elif data =="DuelAmmo1Inc":
                    GM.du.incAmmo(1)
                elif data =="DuelAmmo2Inc":
                    GM.du.incAmmo(2)
                



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