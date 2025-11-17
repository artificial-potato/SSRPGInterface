class Base:
    def __init__(self, interface_instance, stonescript_class_name):
        self._if = interface_instance 
        self._class_name = stonescript_class_name

    def _call(self, method_name, *args, return_type=None):
        full_name = f"{self._class_name}.{method_name}" if self._class_name and method_name else self._class_name or method_name
        return self._if.call(full_name, *args, return_type=return_type)
