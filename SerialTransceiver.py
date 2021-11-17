import json
import time
from serial import Serial
import _thread
import os
class SerialTransceiver:
    def __init__(self,user):
        portinfo = self.getinfo()
        self.user = user
        self.serial = Serial(port=user.port, baudrate=portinfo["baudrate"], bytesize=portinfo["bytesize"], parity=portinfo["parity"])
        

    def getinfo(self) -> dict :
        filename = 'portinfo.json'
        #print(filename)
        f = open(filename)
        lines = f.read()
        infodict = json.loads(s = lines)
        #print(infodict)
        f.close()
        return infodict

    def sendMsg(self):
        ser = self.serial
        # usermsg = input(f'0x0{self.user.instanceID}:')
        usermsg = input()
        print ("\033[A                             \033[A") #清除input的内容 增加美观度 https://stackoverflow.com/questions/10829650/delete-the-last-input-row-in-python
        print(f'0x0{self.user.instanceID} {time.asctime( time.localtime(time.time()))}: {usermsg}')
        ser.write(f'0x0{self.user.instanceID} {time.asctime( time.localtime(time.time()))}: {usermsg}\n'.encode('utf8'))

    def recieve(self) -> str:
        ser = self.serial
        while True:
            if ser.in_waiting > 0:
                # Read data out of the buffer until a carraige return / new line is found
                serialString = ser.readline()
                # Print the contents of the serial data
                try:
                    print(serialString.decode('utf8'),end='')
                except:
                    pass

if __name__ == "__main__":
    # s = SerialTransceiver('/dev/pts/5')
    pass