
import socket
import pickle
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #ONLY EDIT THE NEXT LINE
        self.server = socket.gethostbyname(socket.gethostname())
        #DO NOT EDIT PAST THIS POINT
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        self.client.settimeout(0.01)
    def getInfo(self):
        return self.id
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048*4))

        except socket.error as e:
            print(e)
