"""
SSRPGInterface Python Library v0.11
(for MindConnectProtocol v0.1)

Released under the MIT license
Copyright 2025 ArtificialPotato and contributors
https://github.com/artificial-potato/SSRPGInterface/blob/main/LICENSE
"""
import socket
import itertools
import time
import atexit

class SSRPGInterface:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 64649
        self.step = None
        self.ACK_VER = '\x06' + "0.1"
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(10)
        
        self.connected = False
        atexit.register(self.close)

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

    def call_command(self, *args):
        """
        Send a command to SSRPG.
        """
        self.client.send(("1" + '\x1f' + '\x1f'.join(args)).encode('utf-8'))
        data = self.client.recv(1024)
        if data.decode("utf-8")[2:] == "cmd_done":
            return

    def call(self, *args, raw=False):
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
        if raw:
            return data.decode('utf-8')[2:]
        return self.sloppy_cast(data.decode('utf-8')[2:])

    def multi_call(self, args):
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
        data = self.client.recv(65536)
        return data.decode('utf-8').split('\x1f')[1:]

    def get_screen(self, x, y, w, h):
        """
        Get the screen content from SSRPG.
        """
        inst = [["draw.GetSymbol", x + xy[1], y + xy[0]] for xy in itertools.product(range(h), range(w))]
        res = self.multi_call(inst)
        res = ["".join(res[w * i:w * (i + 1)]) for i in range(h)]
        res = "\n".join(res)
        return res

    def eof(self):
        """
        Notify SSRPG of step completion.
        """
        self.client.send('\x03'.encode('utf-8'))

    def run(self, step=None):
        """
        Start the interface and execute the step function in a loop.
        """
        if not (callable(self.step) or callable(step)):
            print("step() is not callable")
            return #for clarity
        else:
            if step!=None:
                if callable(step):
                    self.step = step
                else:
                    print("The argument step is not callable")
                    return

            self.connect()
            while True:
                try:
                    data = self.client.recv(1024)
                except TimeoutError: # Error when the game is paused
                    print("Connection timed out")
                    continue
                except ConnectionAbortedError:
                    print("Connection closed")
                    self.close()
                    return
                
                if '\x06' in data.decode('utf-8'):
                    if self.ACK_VER != data.decode('utf-8'):
                        print("Warning: version mismatch")
                    self.step()
                    self.eof()
                else:
                    print("error")
                    return
                
    def connect(self):
        print("Connecting to SSRPG")
        while True:
            try:
                self.client.connect((self.host, self.port))
                print("Connected")
                self.connected = True
                return True
            except TimeoutError:
                print("Connection timed out")
            except ConnectionRefusedError:
                print("Connection Refused")

            # retry after 5 seconds
            for i in range(5):
                print("Retry in {} seconds".format(5-i))
                time.sleep(1)
    
    def close(self):
        if self.connected:
            try:
                self.client.send('\x03'.encode('utf-8'))
            except:
                pass
            self.client.close()
            self.connected = False
            print("Connection closed")