# import sys
# import json
import time
from User import User
from SerialTransceiver import SerialTransceiver
import _thread

if __name__ == "__main__":
    # userinfo = getinfo()
    # user = User(int(userinfo['instanceID'],0),userinfo['port'])
    user = User() #获取用户信息
    #user.print()
    serialTransceiver = SerialTransceiver(user)
    _thread.start_new_thread(serialTransceiver.recieve,())
    
   

    while True:
        #time.sleep(1)
        serialTransceiver.sendMsg()
        # usermsg = input(f'0x0{user.instanceID}:')
        # ser.write(f'0x0{user.instanceID} {time.asctime( time.localtime(time.time()))}: {usermsg}\n'.encode('utf8'))
        # # Wait until there is data waiting in the serial buffer
        # if ser.in_waiting > 0:
        #     # Read data out of the buffer until a carraige return / new line is found
        #     serialString = ser.readline()
        #     # Print the contents of the serial data
        #     try:
        #         print(serialString.decode("utf8"))
        #     except:
        #         pass
