"""
SSRPGInterface Python Library v0.1
(for MindConnectProtocol v0.1)

Released under the MIT license
Copyright 2025 ArtificialPotato and contributors
https://github.com/artificial-potato/SSRPGInterface/blob/main/LICENSE
"""
import socket
import itertools

class SSRPGInterface:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 64649
        self.step = None
        self.ack_ver = '\x06' + "0.1"
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sloppy_cast(self, _str):
        """
        Convert string to appropriate type.
        """
        if _str == "":
            return _str
        elif _str == "True":
            return True
        elif _str == "False":
            return False
        elif _str.isdecimal():
            return int(_str)
        elif _str[0] == "-" and _str[1:].isdecimal():
            return -1 * int(_str[1:])
        return _str

    def callcommand(self, *args):
        """
        Send a command to SSRPG.
        """
        self.client.send(("1" + '\x1f' + '\x1f'.join(args)).encode('utf-8'))
        data = self.client.recv(1024)
        if data.decode("utf-8")[2:] == "cmd_done":
            return

    def call(self, *args):
        """
        Call a function or get a variable from SSRPG.
        """
        sendstring = "1" + '\x1f' + str(len(args) - 1) + '\x1f' + args[0]
        for i in range(1, len(args)):
            if type(args[i]) == int:
                sendstring += '\x1f' + "i" + '\x1f' + str(args[i])
            elif type(args[i] == str):
                sendstring += '\x1f' + "s" + '\x1f' + args[i]
            else:
                print("callerr")
                return
        self.client.send(sendstring.encode('utf-8'))
        data = self.client.recv(1024)
        return self.sloppy_cast(data.decode('utf-8')[2:])

    def multcall(self, args):
        """
        Call multiple functions or get multiple variables from SSRPG.
        """
        num = len(args)
        sendstring = str(num)
        for i in range(num):
            sendstring += '\x1f' + str(len(args[i]) - 1) + '\x1f' + args[i][0]
            for j in range(1, len(args[i])):
                if type(args[i][j]) == int:
                    sendstring += '\x1f' + "i" + '\x1f' + str(args[i][j])
                elif type(args[i][j] == str):
                    sendstring += '\x1f' + "s" + '\x1f' + args[i][j]
        self.client.send(sendstring.encode('utf-8'))
        data = self.client.recv(8192)
        return data.decode('utf-8').split('\x1f')[1:]

    def getScreen(self, x, y, w, h):
        """
        Get the screen content from SSRPG.
        """
        inst = [["draw.GetSymbol", x + xy[1], y + xy[0]] for xy in itertools.product(range(h), range(w))]
        res = self.multcall(inst)
        res = ["".join(res[w * i:w * (i + 1)]) for i in range(h)]
        res = "\n".join(res)
        return res

    def eof(self):
        """
        Notify SSRPG of step completion.
        """
        self.client.send('\x03'.encode('utf-8'))

    def run(self):
        """
        Start the interface and execute the step function in a loop.
        """
        if self.step is None:
            print("step() is none")
        else:
            self.client.connect((self.host, self.port))
            try:
                while True:
                    data = self.client.recv(1024)
                    if '\x06' in data.decode('utf-8'):
                        if self.ack_ver != data.decode('utf-8'):
                            print("warn:wrong version")
                        self.step()
                        self.eof()
                    else:
                        print("error")
                        return
            except ConnectionAbortedError:
                print("connection closed")
                return