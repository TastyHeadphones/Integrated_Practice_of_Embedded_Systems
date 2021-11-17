import sys
import json
class User:

   def __init__(self):
      userinfo = self.getinfo()
      self.instanceID = int(userinfo['instanceID'],0)
      self.port = userinfo['port']

   def getinfo(self) -> dict :
      filename = sys.argv[1]
      #print(filename)
      f = open(filename)
      lines = f.read()
      infodict = json.loads(s = lines)
      #print(infodict)
      f.close()
      return infodict
    
   def print(self):
      print(self.instanceID)
      print(self.port)
   
