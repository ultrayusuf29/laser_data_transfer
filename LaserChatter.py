import serial
from threading import Thread
import tkinter
import os

ser=serial.Serial("/dev/pts/3",baudrate=9600,timeout=1.0)
if (ser.isOpen()==False):
    ser.Open()
    print("Port acildi.")
    
ser.flushInput()

readline = lambda : iter(lambda:ser.read(1),"\n")

def send_foto():
        ser.write("<<SENDFILE>>\n")
        ser.write(open("a.jpg","rb").read())
        ser.write("\n<<EOF>>\n")

def send_message():
        x=my_msg.get()
        my_msg.set("")
        if x!='':
            ser.write(x+"\n")
            
def receive_message():
    while 1:
        data="".join(readline())
        if data=="<<SENDFILE>>":
            with open("b.jpg","wb") as outfile:
                while True:
                    line = "".join(readline())
                    if line == "<<EOF>>":
                        break
                    print >> outfile,line
		os.system("viewnior b.jpg")
        else:
            if data:
                msg_list.insert(tkinter.END,data)
                

top=tkinter.Tk()
top.title("LaserChatter")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()
my_msg.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame)
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()
entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send_message)
entry_field.pack()
send_button = tkinter.Button(top, text="Send Messgage",command=send_message)
send_button.pack()
photo_button=tkinter.Button(top, text="Send Photo", command=send_foto)
photo_button.pack()
#top.protocol("WM_DELETE_WINDOW", on_closing)

if __name__=='__main__':
    r=Thread(target=receive_message)
    r.start()
    tkinter.mainloop()
            
            
    
