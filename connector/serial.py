from connector.connector import connectorinterface
import serial
from serial.tools.list_ports import comports


class serialconnector(connectorinterface):

    def __init__(self) -> None:
        super().__init__()
        self.connect()

    def connect(self, dev: str = None):
        if dev is None:
            ports = comports()
            dev = ports[0].device
        if dev is not None:
            self.serial = serial.Serial(dev, 115200, exclusive=True, timeout=0.5, write_timeout=0)

    def disconnect(self):
        return self.serial.close()

    def send(self, data):
        count = self.serial.write(data)
        self.serial.flush()
        return count

    def recv(self, bufsize):
        header = self.serial.read(4)
        readlen = (header[2] << 8) + header[3]
        payload = self.serial.read(readlen)
        data = header + payload
        return data

    def close(self):
        self.serial.close()
