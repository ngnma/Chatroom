import socket
import time
import threading
from tkinter import *
from Ui import *

host='localhost'
port=12348
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
name="unknown"



def send_msg():
    msg = entry.get()
    create_message_ui(canvas, msg, name, False, chosen)
    msg = msg + str("%") + str(name)
    msg = msg.encode()
    client.send(msg)
    entry.delete(0, END)

def recv_msg():
    while True:
        message = client.recv(1024).decode()
        msg,name=message.split('%')
        name=name[2:-1]
        create_message_ui(canvas, msg, name, True, chosen)

def get_name():
    name = input("name:").encode()
    client.send(name)
    return name

name=get_name()
chosen=input("theme:\n1.Dark\n2.Light\n3.Classic Dark\n4.Classic Light\ninput:")



# init ui
root = Tk()
root.geometry("300x600")
root.resizable(width=False, height=False)
root.title(name)


canvas = Canvas(root)
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
frame = Frame(canvas)
canvas.configure(bg='#D3D3D3')  # light-default
entry = Entry(root)
btn = Button(root, text="send",command=send_msg)

pack_widgets(entry,btn,canvas,scrollbar,frame)


threading.Thread(target=recv_msg).start()
# threading.Thread(target=send_msg).start()

root.mainloop()
