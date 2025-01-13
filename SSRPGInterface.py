import socket
import select

class SSRPGInterface:
    def __init__(self):
        self.host="127.0.0.1"
        self.port=12312
        self.step=None
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def callcommand(self,*args):
        self.client.send(";".join(args).encode('utf-8'))
        data = self.client.recv(1024)
        if data.decode("utf-8")=="cmd_executed":
            return
    def call(self,*args):
        self.client.send(";".join(args).encode('utf-8'))
        data = self.client.recv(1024)
        print(data.decode('utf-8'))
        return data.decode('utf-8')[4:]
    def eof(self):
        self.client.send("EOF".encode('utf-8'))
    def run(self):
        if self.step==None:
            print("step() is none")
        else:
            self.client.connect((self.host, self.port))
            try:
                while True:
                    data = self.client.recv(1024)
                    if "start_step"==data.decode('utf-8'):
                        self.step()
                    else:
                        print("error")
            except ConnectionAbortedError:
                print("connection closed")
                return
