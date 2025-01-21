"""
SSRPGInterface Python Library v0.11
(for MindConnectProtocol v0.1)

Released under the MIT license
Copyright 2025 ArtificialPotato and contributors
https://github.com/artificial-potato/SSRPGInterface/blob/main/LICENSE
"""
import sys
import socket
import itertools
import time
import atexit

from .cache import preload

DELIMITER = "\x1f"
ACK_VER = '\x06' + "0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(10)

connecting = False

def send(str_list) -> None:
    client.send(DELIMITER.join(str_list).encode('utf-8'))

def param_process(arg) -> list[str, str]:
    if arg is None:
        return None
    if type(arg) is int:
        return ["i", str(arg)]
    if type(arg) is bool:
        return ["s", "True" if arg else "False"]
    if type(arg) is str:
        return ["s", arg]
    
def command_process(name, args) -> list[str]:
    send_str_list = [str(len(args)), name]
    for arg in args:
        send_arg_str_list = param_process(arg)
        if send_arg_str_list is None:
            print(f"Call {name} Command Error. args: {args}")
            return None
        send_str_list += send_arg_str_list
    return send_str_list

def sloppy_cast(_str):
    """
    Convert string to appropriate type.
    """

    if _str == "":
        return ""
    elif _str == "True":
        return True
    elif _str == "False":
        return False
    elif _str.isdecimal():
        return int(_str)
    elif _str[0] == "-" and _str[1:].isdecimal():
        return -1 * int(_str[1:])
    return _str

def call_command(name:str, *args):
    """
    Send a command to SSRPG.
    """
    if len(args) == 1 and type(args[0]) == list:
        args = args[0]
    send(["1", name] + list(args))
    data = client.recv(1024)
    if data.decode("utf-8")[2:] == "cmd_done":
        return

def call(name:str, *args):
    """
    Call a function or get a variable from SSRPG.
    """

    send_str_list = command_process(name, args)
    if send_str_list is None:
        return
    send_str_list = ["1"] + send_str_list

    send(send_str_list)
    data = client.recv(1024)
    return data.decode('utf-8')[2:]

def multi_call(command_list:list):
    """
    Call multiple functions or get multiple variables from SSRPG.
    """

    send_str_list = [str(len(command_list))]
    for command in command_list:
        command_send_str_list = command_process(command[0], command[1:])
        if command_send_str_list is None:
            return
        send_str_list += command_send_str_list

    send(send_str_list)
    data = client.recv(65536)
    return data.decode('utf-8').split(DELIMITER)[1:]

def get_screen(x, y, w, h):
    """
    Get the screen content from SSRPG.
    """
    inst = [["draw.GetSymbol", x + xy[1], y + xy[0]] for xy in itertools.product(range(h), range(w))]
    res = multi_call(inst)
    res = ["".join(res[w * i:w * (i + 1)]) for i in range(h)]
    res = "\n".join(res)
    return res

def connect(host="127.0.0.1", port=64649):
    global connecting
    print("Start Connect SSRPG")
    while True:
        print("\rConnecting          ", end="")
        print("\r", end="")
        try:
            client.connect((host, port))
            print("\rConnect Success")
            connecting = True
            return True
        except TimeoutError:
            print("\rConnect Timeout", end="")
        except ConnectionRefusedError:
            print("\rConnect Refused", end="")

        # retry after 5 seconds
        for i in range(5):
            print(".", end="")
            sys.stdout.flush()
            time.sleep(1)

def eof():
    """
    Notify SSRPG of step completion.
    """
    client.send('\x03'.encode('utf-8'))

def close():
    global connecting
    if connecting:
        client.close()
        connecting = False
        print("Close Connect")

def run(step, host="127.0.0.1", port=64649):
    """
    Start the interface and execute the step function in a loop.
    """

    atexit.register(close)
    connect(host, port)

    while True:
        try:
            data = client.recv(1024)
        except TimeoutError: # Error when the game is paused
            print("\rOperation timeout", end="")
            continue
        except ConnectionAbortedError:
            print("\nConnection Closed")
            close()
            return
        except Exception:
            print(Exception)
            print("An unexpected error occurred, exiting the program")
            close()
            return

        if '\x06' in data.decode('utf-8'):
            if ACK_VER != data.decode('utf-8'):
                print("Warning: version mismatch")
            preload()
            step()
            eof()
        else:
            print("error")
            return