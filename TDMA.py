import time

def Send(interval,sendFunc):
    while(True):
        if(time.time() % 60 % 2  == interval):
            sendFunc()
            return

if __name__ == "__main__":
    Send(0,lambda : print(time.time() % 60))

    



