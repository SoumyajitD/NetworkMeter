from tkinter import *
import pyspeedtest
from PIL import ImageTk, Image
import tkinter.messagebox as tmsg
import speedtest
root=Tk()

root.title("Network Monitor v1.0")



def ping():
    st=pyspeedtest.SpeedTest("www.google.com")
    pingv="Your Ping is %0.2fms" %st.ping()
    tmsg.showinfo("Ping Test Results",pingv)

def down():
    st=pyspeedtest.SpeedTest("www.google.com")
    downvmb=(st.download()/10240)
    downv="Your Download Speed is %0.2fMB" %downvmb
    tmsg.showinfo("Download Test Results",downv)

def up():
    wifi  = speedtest.Speedtest() 

    upmb=wifi.upload ()/1024000
    upv="Your Upload Speed is %0.2fMB" %upmb
    tmsg.showinfo("Upload Test Results",upv)




root.geometry("897x501")
root.minsize(473,250)
root.maxsize(897,501)
f1=Frame(root,borderwidth=2)
f1.pack(fill=X)
fside=Frame(root,pady=110)
fside.pack(side=RIGHT)

navText=Label(f1,text="Network Monitor Tool",font="Calibri 20 bold",padx=700,bg="black",fg="white",pady=20)
navText.pack()

# ip=StringVar()
# city=StringVar()

# ip=Entry(fside,textvariable=ip).pack()
# city=Entry(fside,textvariable=city).pack()


pane = Frame(root,pady=50,borderwidth=2,bg="white")
pane.pack(side=BOTTOM,fill = X)
 

pingB= Button(pane, text = "PING",background = "red", fg = "white",font="Calibri 14 bold",command=ping)
pingB.pack(side = LEFT, expand = True, fill = X)
 

downB = Button(pane, text = "DOWNLOAD SPEED",background = "blue", fg = "white",font="Calibri 14 bold",command=down)
downB.pack(side=LEFT, expand = True, fill = X)
 
upB = Button(pane, text = "UPLOAD SPEED", background = "green", fg = "white",font="Calibri 14 bold", command=up)
upB.pack(side = LEFT, expand = True, fill = X)





root.mainloop()
