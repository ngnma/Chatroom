from datetime import datetime
from tkinter import *
from tkinter import ttk

def pack_widgets(entry,btn,canvas,scrollbar,frame):
    entry.pack(side=BOTTOM, fill=X)
    btn.pack(fill=X, side=BOTTOM)
    canvas.pack(fill="both", side="left", expand=True, anchor="e")
    scrollbar.pack(fill=Y, side="right")
    canvas.create_window(0, 0, anchor='nw', window=frame)
    canvas.update_idletasks()


def message_ui(canvas,msg, name, light_color, dark_color, text_color, labelanchor_lframe, anchor_msg, anchor_time):
    labelframe = LabelFrame(canvas, height=100, width=200, text=name, bg=dark_color, fg=text_color, relief=FLAT,
                            labelanchor=labelanchor_lframe)
    labelframe.pack(side=TOP, padx=10, pady=5, anchor=anchor_msg)
    lable_msg = Label(labelframe, text=msg, bg=light_color, )
    lable_msg.config(wraplength=150)
    lable_msg.config(justify=LEFT)
    lable_msg.pack()
    lable_time = Label(labelframe, text=datetime.now().strftime('%H:%M'), bg=dark_color,
                       font="lucida 10 bold", fg=text_color
                       )
    lable_time.pack(anchor=anchor_time)


p1 = 'Bob'
p2 = 'Tom'
msg = "Do you know what time it is?"
msg2 = "its morning in Tokyo!"


def classic_theme_dark(canvas,msg,name,main_theme):
    canvas.configure(bg='#7F6E50')  # classic dark
    if main_theme:
        message_ui(canvas,msg, name, "#D3D3D3", "#A9A9A9", "black", 'nw', 'w', 'e')
    else:
        message_ui(canvas,msg, name, "#FAD5A5", "#DAA06D", "#8B4000", 'ne', 'e', 'w')


def classic_theme_light(canvas,msg,name,main_theme):
    canvas.configure(bg='#F5DEB3')  # classic light
    if main_theme:
        message_ui(canvas,msg, name, "#D3D3D3", "#A9A9A9", "black", 'nw', 'w', 'e')
    else:
        message_ui(canvas,msg, name, "#FAD5A5", "#DAA06D", "#8B4000", 'ne', 'e', 'w')


def dark_theme(canvas,msg,name,main_theme):
    canvas.configure(bg='#1B2134')  # dark
    if main_theme:
        message_ui(canvas,msg, name, "#7F90D9", "#5466A9", "white", 'nw', 'w', 'e')
    else:
        message_ui(canvas,msg, name, "#5466A9", "#424C6F", "#7F90D9", 'ne', 'e', 'w')


def light_theme(canvas,msg,name,main_theme):
    canvas.configure(bg='#D3D3D3')  # light
    if main_theme:
        message_ui(canvas,msg, name, "#E0FFFF", "#AFEEEE", "#4682B4", 'nw', 'w', 'e')
    else:
        message_ui(canvas,msg, name, "#FFF8DC", "#F5DEB3", "#C70039", 'ne', 'e', 'w')

def create_message_ui(canvas,msg,name,main_theme,chosen):
    if chosen=='1':
        dark_theme(canvas,msg,name,main_theme)
    elif chosen=='2':
        light_theme(canvas,msg,name,main_theme)
    elif chosen=='3':
        classic_theme_dark(canvas,msg,name,main_theme)
    else:
        classic_theme_light(canvas,msg,name,main_theme)
