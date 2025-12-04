import threading
from typing import Callable, Generic, TypeVar, ParamSpec

P = ParamSpec("P") # func parameter types
R = TypeVar("R") # return type 

class Signal(Generic[P, R]):
    def __init__(self) -> None:
        self._connections: list[Connection[P, R]] = []


    def connect(self, callback: Callable[P, R]) -> "Connection[P, R]":
        conn = Connection(self, callback)
        self._connections.append(conn)
        return conn
    
    def once(self, callback: Callable[P, R]) -> "Connection[P, R]":
        def wrapper(*args, **kwargs):
            result = callback(*args, **kwargs)
            conn.disconnect()
            return result

        conn = self.connect(wrapper) 
        return conn
    

    def Emit(self, *args: P.args, **kwargs: P.kwargs) -> None:
        for conn in list(self._connections):
            t = threading.Thread(
                target=conn.callback,
                args=args,
                kwargs=kwargs,
                daemon=True
            )
            t.start()


    def disconnect_all(self) -> None:
        self._connections.clear()


    def _remove_connection(self, conn: "Connection[P, R]") -> None:
        self._connections.remove(conn)


class Connection(Generic[P, R]):
    def __init__(self, signal: Signal[P, R], callback: Callable[P, R]) -> None:
        self.signal = signal
        self.callback = callback

    def disconnect(self) -> None:
        self.signal._remove_connection(self)