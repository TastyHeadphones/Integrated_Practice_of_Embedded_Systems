from serial import Serial

ser = Serial("/dev/pts/5") #or whatever 
readline = lambda : iter(lambda:ser.read(1),"\n")

while "".join(readline()) != "<<SENDFILE>>": #wait for client to request file
    pass #do nothing ... just waiting ... we could time.sleep() if we didnt want to constantly loop
ser.write(open("some_file.txt","rb").read()) #send file
ser.write("\n<<EOF>>\n") #send message indicating file transmission complete