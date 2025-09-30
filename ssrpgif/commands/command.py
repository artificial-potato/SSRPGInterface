class Command:
    def __init__(self, interface_instance):
        self._if = interface_instance
        self._command_queue = []

    def clear_queue(self):
        self._command_queue.clear()

    def run_queued_commands(self):
        if not self._command_queue:
            return
        self._if.multi_call(self._command_queue)

    def _queue_command(self, name, *args):
        self._command_queue.append([name] + list(args))

    def Print(self, *args, x: int = None, y: int = None, color: str = None, face: bool = False, player: bool = False, head: bool = False, foe: bool = False, center: bool = False):
        str_list = []
        if face:
            str_list.append("(")
        elif isinstance(x, int) and isinstance(y, int):
            prefix = ''
            if player:
                prefix = "o"
            elif head:
                prefix = "h"
            elif foe:
                prefix = "f"
            elif center:
                prefix = "c"
            else:
                prefix = "`"
            str_list.append(f'{prefix}{x},{y},')
            if color:
                str_list.append(f'{color},')
        str_list.extend(map(str, args))
        self._queue_command(">", "".join(str_list))

    def Play(self, *args):
        self._queue_command("play", " ".join(map(str, args)))

    def EquipR(self, *args: str):
        self._queue_command("equipR", " ".join(args))

    def EquipL(self, *args: str):
        self._queue_command("equipL", " ".join(args))

    def Equip(self, *args: str):
        self._queue_command("equip", " ".join(args))

    def Loadout(self, index: int):
        self._queue_command("loadout", str(index))

    def Activate(self, *args):
        self._queue_command("activate", " ".join(map(str, args)))

    def Enable(self, *args):
        self._queue_command("enable", " ".join(args))

    def Disable(self, *args):
        self._queue_command("disable", " ".join(args))

    def Brew(self, *args: str):
        self._queue_command("brew", "+".join(args))
