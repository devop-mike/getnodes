from connector.connector import connectorinterface
import socket
import time


class socketconnector(connectorinterface):

    def __init__(self, dest: str) -> None:
        super().__init__()
        self.connect(dest)

    def connect(self, dest: str):
        self.socket = socket.create_connection((dest, 4403))
        # send wake up
        buf = bytearray([0xFF] * 8)
        self.send(buf)
        time.sleep(0.1)

    def disconnect(self):
        return self.socket.close()

    def send(self, data):
        return self.socket.send(data)

    def recv(self, bufsize):
        return self.socket.recv(bufsize)

    def close(self):
        self.socket.close()
