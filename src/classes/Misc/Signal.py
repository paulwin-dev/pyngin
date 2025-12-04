class Signal:
    def __init__(self) -> None:
        self._connections = []

    def Connect(self):
        pass

    def Once(self):
        pass

    def DisconnectAll(self):
        pass

    def _removeConnection(self, connection: "Connection"):
        self._connections.remove(connection)


class Connection:
    def __init__(self, signal: "Signal") -> None:
        self._signal = signal

    def Disconnect(self):
        self._signal._removeConnection(self)