import json
from serial import Serial

class SerialTransceiver:
    def __init__(self,port):
        portinfo = self.getinfo()
        self.serial = Serial(port=port, baudrate=portinfo["baudrate"], bytesize=portinfo["bytesize"], parity=portinfo["parity"])
        Serial()

    def getinfo(self) -> dict :
        filename = 'portinfo.json'
        #print(filename)
        f = open(filename)
        lines = f.read()
        infodict = json.loads(s = lines)
        print(infodict)
        f.close()
        return infodict

if __name__ == "__main__":
    s = SerialTransceiver('/dev/pts/5')
