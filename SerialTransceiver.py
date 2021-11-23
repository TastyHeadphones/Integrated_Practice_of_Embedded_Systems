import json
import time
from serial import Serial
import _thread
import os
import TDMA
import packge
class SerialTransceiver:
    def __init__(self,user):
        portinfo = self.getinfo()
        self.user = user
        self.serial = Serial(port=user.port, baudrate=portinfo["baudrate"], bytesize=portinfo["bytesize"], parity=portinfo["parity"])
        TDMA.Send(self.user.instanceID,lambda: self.serial.write(f'0x0{self.user.instanceID} {time.asctime( time.localtime(time.time()))} is online\n'.encode('utf8')))       


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
        def serWrite():
            TDMA.Send(self.user.instanceID,lambda: ser.write(f'0x0{self.user.instanceID} {time.asctime( time.localtime(time.time()))}: {usermsg}\n'.encode('utf8')))
            print(f'0x0{self.user.instanceID} {time.asctime( time.localtime(time.time()))}: {usermsg}')
        def sendFile(sourceID,file):
            _thread.start_new_thread(serWrite,())
            if sourceID == 0:
                packge.split_file(file)

            elif sourceID == 1:
                packge.cat_files(file)
        ser = self.serial
        # usermsg = input(f'0x0{self.user.instanceID}:')
        usermsg = input()
        if usermsg[0:5] == 'file:':
            fileName = usermsg.split(":")[1]     
            sendFile(self.user.instanceID,fileName)
        else:
            print ("\033[A                             \033[A") #清除input的内容 增加美观度 https://stackoverflow.com/questions/10829650/delete-the-last-input-row-in-python
            _thread.start_new_thread(serWrite,())
        # ser.write(f'0x0{self.user.instanceID} {time.asctime( time.localtime(time.time()))}: {usermsg}\n'.encode('utf8'))

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
    
    def sendFile(self):
        pass

if __name__ == "__main__":
    # s = SerialTransceiver('/dev/pts/5')
    pass