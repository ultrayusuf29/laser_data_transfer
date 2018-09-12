from serial import Serial
ser = Serial("/dev/pts/4") #or whatever 
ser.write("<<SENDFILE>>\n") #tell server we are ready to recieve
readline = lambda : iter(lambda:ser.read(1),"\n")
with open("b.jpg","wb") as outfile:
   while True:
       line = "".join(readline())
       if line == "<<EOF>>":
           break #done so stop accumulating lines
       print >> outfile,line
