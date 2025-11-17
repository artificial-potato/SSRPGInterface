from .base import Base

class Variable(Base):
    def __init__(self, interface_instance):
        # The 'var' class in stonescript is special (Do not use cache)
        super().__init__(interface_instance, "") 
        self._if = interface_instance

    def __setitem__(self, key: str, value):
        self._if.call("var.set", key, value)

    def __getitem__(self, key: str):
        # Use a direct call for var.get as it retrieves data
        return self._if.call("var.get", key)

    def __contains__(self, key: str) -> bool:
        return self._if.call("var.has", key, return_type=bool)
