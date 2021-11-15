import sys
import json


if __name__ == "__main__":
    filename = sys.argv[1]
    print(filename)
    f = open(filename)
    lines = f.read()
    dicta = json.loads(s = lines)
    print(dicta)
    f.close()