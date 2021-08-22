import socket
import threading

host='localhost'
port=12348

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
print('server listening...')
server.listen(5)

def recv_msg(con,addr,name):
    while True:
        msg=con.recv(1024)
        for item in cons:
            # item.send(name)
            if item is not con:
                item.send(msg)

def new_client(con,addr):
    name=con.recv(1024)
    threading.Thread(target=recv_msg, args=(con, addr,name)).start()

# def send_all():
#     while True:
#         msg=input("msg to all:").encode()
#         for item in cons:
#             item.send(msg)
cons=set()
# threading.Thread(target=send_all).start()

while True:
    con, addr = server.accept()
    cons.add(con)
    print(f'server is connected to {addr[1]}')
    threading.Thread(target=new_client, args=(con,addr)).start()









