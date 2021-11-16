import sys
import json

def getinfo() -> dict :
    filename = sys.argv[1]
    print(filename)
    f = open(filename)
    lines = f.read()
    infodict = json.loads(s = lines)
    print(infodict)
    f.close()
    return infodict

if __name__ == "__main__":
    userinfo = getinfo()