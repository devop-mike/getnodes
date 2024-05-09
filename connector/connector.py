import socket
import time


class connectorinterface:
    def __init__(self) -> None:
        pass

    def connect(self):
        raise NotImplementedError

    def disconnect(self):
        raise NotImplementedError

    def send(self, data):
        raise NotImplementedError

    def recv(self, bufsize):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError


class psudoconnector(connectorinterface):
    def __init__(self) -> None:
        super().__init__()
