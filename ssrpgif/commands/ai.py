from .base import Base

class AI(Base):
    def __init__(self, interface_instance):
        super().__init__(interface_instance, "ai")

    def enabled(self) -> bool:
        return self._call("enabled", return_type=bool)

    def paused(self) -> bool:
        return self._call("paused", return_type=bool)

    def idle(self) -> bool:
        return self._call("idle", return_type=bool)

    def walking(self) -> bool:
        return self._call("walking", return_type=bool)
