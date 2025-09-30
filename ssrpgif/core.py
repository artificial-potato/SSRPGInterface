import socket
import threading
import re
import time
import itertools
from . import commands
from typing import Callable

class SSRPGInterface:
    """
    Main interface for interacting with StoneStoryRPG via MindConnect protocol v0.3.
    """
    PROTOCOL_VERSION = "0.3"

    def __init__(self, mode='sync', host="127.0.0.1", port=64649):
        if mode not in ['sync', 'async', 'exclusive']:
            raise ValueError("Mode must be one of 'sync', 'async', or 'exclusive'")
        
        self._mode = mode
        self._client = _MindConnectClient(self, host, port)
        self._async_callbacks = {}

        # --- Integrated features ---
        self.cache = _CacheManager(self)
        
        self.command = commands.command.Command(self)
        #commands
        self.print=self.command.Print
        self.play=self.command.Play
        self.equipR=self.command.EquipR
        self.equipL=self.command.EquipL
        self.equip=self.command.Equip
        self.loadout=self.command.Loadout
        self.activate=self.command.Activate
        self.enable=self.command.Enable
        self.disable=self.command.Disable
        self.brew=self.command.Brew
        #
        self.ai = commands.ai.AI(self)
        self.character = commands.character.Character(self)
        self.draw = commands.draw.Draw(self)
        self.encounter = commands.encounter.Encounter(self)
        self.event = commands.event.Event(self)
        self.foe = commands.foe.Foe(self)
        self.harvest = commands.harvest.Harvest(self)
        self.input = commands.input.Input(self)
        self.item = commands.item.Item(self)
        #has not yet been activated
        #self.key = commands.key.Key(self)
        self.loc = commands.loc.Loc(self)
        self.pickup = commands.pickup.Pickup(self)
        self.player = commands.player.Player(self)
        self.pos = commands.pos.Position(self)
        self.res = commands.res.Resource(self)
        self.screen = commands.screen.Screen(self)
        #have to implement InvocationContext
        #self.storage = commands.storage.Storage(self)
        self.summon = commands.summon.Summon(self)
        #self.text = commands.text.Text(self)
        self.armor = commands.armor.Armor(self)
        self.var = commands.var.Variable(self)

        #toplevel vars
        self.time: Callable[[],int] = lambda :self.call("time", return_type=int)
        self.totaltime: Callable[[],int] = lambda :self.call("totaltime", return_type=int)
        self.hp: Callable[[],int] = lambda :self.call("hp", return_type=int)
        self.maxhp: Callable[[],int] = lambda :self.call("maxhp", return_type=int)
        self.maxarmor: Callable[[],int] = lambda :self.call("maxarmor", return_type=int)
        self.face: Callable[[],str] = lambda :self.call("face", return_type=str)
        self.bighead: Callable[[],bool] = lambda :self.call("bighead", return_type=bool)
        self.totalgp: Callable[[],int] = lambda :self.call("totalgp", return_type=int)




    def connect(self, timeout=10):
        """Establishes a connection to the game."""
        self._client.connect(timeout)
        if self._mode == 'async':
            self._client.start_async_listener(self._on_async_response)

    def disconnect(self):
        """Disconnects from the game."""
        self._client.close()

    def _on_async_response(self, request_id, response_data):
        if request_id in self._async_callbacks:
            callback = self._async_callbacks.pop(request_id)
            callback(response_data)

    def step(self, step_function):
        """
        Executes one step of processing for 'sync' and 'exclusive' modes.
        """
        if self._mode == 'async':
            raise RuntimeError("step() is only for 'sync' and 'exclusive' modes.")
            
        context, version = self._client.wait_for_signal()
        if version and version != self.PROTOCOL_VERSION:
            print(f"Warning: Protocol version mismatch! Client is v{self.PROTOCOL_VERSION}, Server is v{version}")

        if context:
            try:
                self.cache.clear()
                self.command.clear_queue()
                step_function(context)
                self.command.run_queued_commands()
            finally:
                self._client.send_eof()

    def _sloppy_cast(self, s, target_type=None):
        if s is None or s == "": return None
        if target_type is bool: return s == 'True'
        if target_type is int:
            if s.startswith('-') and s[1:].isdigit(): return int(s)
            if s.isdigit(): return int(s)
            return None # Conversion failed
        if target_type is None:
            if s == "True": return True
            if s == "False": return False
            if s.startswith('-') and s[1:].isdigit(): return int(s)
            if s.isdigit(): return int(s)
        return s # str or other

    def call(self, command, *args, return_type=None):
        key = (command,) + args
        if key in self.cache._cache_dict:
            return self.cache._cache_dict[key]

        response = self._client.send_and_receive_sync([[command] + list(args)])
        result = response[0] if response else None
        
        self.cache._cache_dict[key] = result
        return result

    def call_async(self, requests, callback):
        """
        Sends a request in 'async' mode without waiting for a response.
        """
        if self._mode != 'async':
            raise RuntimeError("call_async() is only for 'async' mode.")
        
        request_id = self._client.send_request(requests)
        self._async_callbacks[request_id] = callback

    def multi_call(self, requests):
        """
        Synchronously sends multiple requests and waits for the response.
        """
        if self._mode == 'async':
            raise RuntimeError("multi_call is designed for sync/exclusive modes. Use call_async for async.")
        
        return self._client.send_and_receive_sync(requests)

    def get_screen(self, x, y, w, h):
        """Retrieves a portion of the game screen as text."""
        requests = [["draw.GetSymbol", x + col, y + row] for row in range(h) for col in range(w)]
        raw_symbols = self.multi_call(requests)
        return '\n'.join(''.join(raw_symbols[i:i+w]) for i in range(0, len(raw_symbols), w))

class _MindConnectClient:
    # Internal class handling low-level protocol details.
    def __init__(self, interface, host, port):
        self._if = interface
        self._host = host
        self._port = port
        self._sock = None
        self._request_id_counter = 0
        self._lock = threading.Lock()
        self._running = False
        self._listener_thread = None
        self._async_response_callbacks = {}

    def connect(self, timeout):
        try:
            self._sock = socket.create_connection((self._host, self._port), timeout)
            self._running = True
        except socket.error as e:
            raise ConnectionError(f"Failed to connect to {self._host}:{self._port}: {e}")

    def close(self):
        self._running = False
        if self._sock:
            try:
                self._sock.shutdown(socket.SHUT_RDWR)
            except socket.error:
                pass
            finally:
                self._sock.close()
                self._sock = None
        if self._listener_thread and self._listener_thread.is_alive():
            self._listener_thread.join()

    def _next_request_id(self):
        with self._lock:
            self._request_id_counter = (self._request_id_counter + 1) % 10000
            return self._request_id_counter

    def _build_packet(self, request_id, requests):
        parts = [str(request_id), str(len(requests))]
        for req in requests:
            if not isinstance(req, (list, tuple)) or not req:
                raise TypeError(f"Invalid request format: {req}. Requests must be non-empty lists or tuples.")
            
            name = req[0]
            args = req[1:]
            
            # For commands, the protocol is simpler.
            # Check if it's a command from the module.
            if name in [">", "play", "equipR", "equipL", "equip", "loadout", "activate", "enable", "disable", "brew"]:
                 parts.append("1")
                 parts.extend(req)
            else: # For function/variable calls
                parts.append(str(len(args)))
                parts.append(name)
                for arg in args:
                    if isinstance(arg, int):
                        parts.extend(['i', str(arg)])
                    else:
                        parts.extend(['s', str(arg)])
        #print(parts)
        return '\x1f'.join(parts).encode('utf-8')

    def send_request(self, requests):
        if not self._sock:
            raise ConnectionError("Not connected.")
        req_id = self._next_request_id()
        packet = self._build_packet(req_id, requests)
        self._sock.sendall(packet)
        return req_id

    def send_and_receive_sync(self, requests):
        req_id = self._next_request_id()
        packet = self._build_packet(req_id, requests)
        with self._lock:
            if not self._sock:
                raise ConnectionError("Not connected.")
            self._sock.sendall(packet)
            raw_data = self._receive_data()
        if raw_data:
            parsed_id, responses = self._parse_response(raw_data)
            if parsed_id == req_id:
                return responses
            else:
                raise ConnectionAbortedError("Wrong response ID.")
                # return self.send_and_receive_sync(requests)
        raise ConnectionAbortedError("Did not receive a response from the server.")

    def send_eof(self):
        if not self._sock: return
        try:
            self._sock.sendall(b'\x03')
        except socket.error:
            pass

    def _receive_data(self):
        try:
            # Increased buffer size for large multi_call responses
            data = self._sock.recv(65536)
            if not data:
                self.close()
                return None
            return data.decode('utf-8')
        except socket.error:
            self.close()
            return None

    def _parse_response(self, raw_data):
        try:
            parts = raw_data.split('\x1f')
            req_id = int(parts[0])
            # The number of results is in parts[1], so the actual results start from index 2
            responses = [self._if._sloppy_cast(p, None) for p in parts[1:]]
            return req_id, responses
        except (ValueError, IndexError) as e:
            raise ConnectionAbortedError(f"Failed to parse server response: {raw_data} ({e})")

    def wait_for_signal(self):
        raw_data = self._receive_data()
        if not raw_data: return None, None

        if raw_data.startswith('\x06'):
            signal_body = raw_data[1:]
            match = re.match(r"(pre|post)?(\d+\.\d+)", signal_body)
            if match:
                context = match.group(1) if match.group(1) else "exclusive"
                version = match.group(2)
                return context, version
            else: # Fallback for older versions without version in signal
                return signal_body if signal_body else "exclusive", None
        
        raise ConnectionAbortedError(f"Expected a step signal (\x06), but got: {raw_data[:50]}")

    def start_async_listener(self, callback_handler):
        self._async_response_callbacks["handler"] = callback_handler
        self._listener_thread = threading.Thread(target=self._async_listener_loop)
        self._listener_thread.daemon = True
        self._listener_thread.start()

    def _async_listener_loop(self):
        buffer = ""
        while self._running:
            try:
                data = self._sock.recv(4096).decode('utf-8')
                if not data: break
                buffer += data
                # This part might need improvement based on real-world async usage.
                if '\x1f' in buffer: # A simple check for a delimiter
                    response_data = buffer
                    buffer = ""
                    req_id, responses = self._parse_response(response_data)
                    handler = self._async_response_callbacks.get("handler")
                    if handler:
                        handler(req_id, responses)
            except socket.error:
                break
        self._running = False

class _CacheManager:
    def __init__(self, interface_instance):
        self._if = interface_instance
        self._cache_dict = {}

    def clear(self):
        self._cache_dict.clear()
