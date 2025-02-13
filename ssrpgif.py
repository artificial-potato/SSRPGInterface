"""
SSRPGInterface Python Library v0.11
(for MindConnectProtocol v0.1)

Released under the MIT license
Copyright 2025 ArtificialPotato and contributors
https://github.com/artificial-potato/SSRPGInterface/blob/main/LICENSE
"""

import socket
from atexit import register
from sys import stdout
from time import sleep

DELIMITER = "\x1f"
ACK = "\x06"
API_VERSION = "0.1"

Game_Version:str = None

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(10)

def recv(size:int=1024):
    while True:
        try:
            data = client.recv(size)
            return data.decode("utf-8")
        except TimeoutError:
            # Error when the game is paused or left a location
            print("\rOperation timeout", end="")
            continue
        except ConnectionAbortedError:
            print("\nConnection Closed")
            exit()
        except Exception as e:
            print(e)
            print("An unexpected error occurred, exiting the program")
            exit()

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
    return None
    
def command_process(name, args) -> list[str]:
    send_str_list = [str(len(args)), name]
    for arg in args:
        send_arg_str_list = param_process(arg)
        if send_arg_str_list is None:
            print(f"Call {name} Command Error. args: {args}")
            return None
        send_str_list += send_arg_str_list
    return send_str_list

def sloppy_cast(v, t=None):
    """
    Convert string to appropriate type.
    """
    
    if t is int:
        return int(v)
    if t is bool:
        return False if v == "False" or not v else True
    return v



def call_command(name:str, *args):
    """
    Send a command to SSRPG.
    """

    # if len(args) == 1 and type(args[0]) == list:
    #     args = args[0]
    send(["1", name] + list(args))
    data = recv().split(DELIMITER)[1:]
    if data[0] != "cmd_done":
        print(f"command error. name:{name}, args:{args}")

def multi_call_command(command_list:list[dict]):
    length = len(command_list)
    send_str_list = [str(length)]
    for command in command_list:
        send_str_list += [command["name"]] + list(command["args"])

    send(send_str_list)
    data = recv()
    result_list = data.split(DELIMITER)[1:]
    for i in range(length):
        if result_list[i] != "cmd_done":
            name, args = command_list[i].items()
            print(f"command error. name:{name}, args:{args}")


def call(name:str, *args, return_type=None):
    """
    Call a function or get a variable from SSRPG.
    """

    send_str_list = command_process(name, args)
    if send_str_list is None:
        return
    send_str_list = ["1"] + send_str_list

    send(send_str_list)
    data = recv()
    return sloppy_cast(data.split(DELIMITER)[1], return_type)

def multi_call(command_list:list[dict]):
    """
    ```
    [
        {
            'name' : str,
            'args' : *,
            'return_type': int|bool|str
        }, ...
    ]
    ```

    Call multiple functions or get multiple variables from SSRPG.
    """

    send_str_list = [str(len(command_list))]
    for command in command_list:
        command_send_str_list = command_process(command["name"], command["args"])
        if command_send_str_list is None:
            return
        send_str_list += command_send_str_list

    send(send_str_list)
    data = recv(65536)

    result = data.split(DELIMITER)[1:]
    for i in range(len(result)):
        result[i] = sloppy_cast(result[i], command_list[i]["return_type"])
    return result


def connect(host="127.0.0.1", port=64649):
    print("Start Connect SSRPG")
    while True:
        print("\rConnecting          ", end="")
        print("\r", end="")
        try:
            client.connect((host, port))
            break
        except TimeoutError:
            print("\rConnect Timeout", end="")
        except ConnectionRefusedError:
            print("\rConnect Refused", end="")

        # retry after 5 seconds
        for _ in range(5):
            print(".", end="")
            stdout.flush()
            sleep(1)

    register(close)
    print("\rConnect Success")
    return True

def check_header() -> bool:
    data = recv(256)
    if data and data[0] == ACK:
        data = data[1:].split(DELIMITER)
        if data[0] != API_VERSION:
            print("Warning: version mismatch")
        # Game_Version = data[1]
        return True
    else:
        print("error")
        return False
    
def check_response() -> bool:
    data = recv(256)
    if data and data[0] == ACK:
        # match data[1:]:
        #     case _:
        #         pass
        return True
    else:
        print("error")
        return False

def send_eof():
    """
    Notify SSRPG of step completion.
    """
    client.send('\x03'.encode('utf-8'))

def close():
    call("loc.Pause")
    client.close()
    print("Close Connect")

def run(step):
    """
    Start the interface and execute the step function in a loop.
    """

    from .cache import preload, run_command

    if check_header():
        while True:
            preload()
            step()
            run_command()
            send_eof()

            if not check_response():
                break
    # exit()