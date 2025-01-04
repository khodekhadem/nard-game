import socket
import threading
import time
import random

def clear_online_clients():
    while True:
        time.sleep(5)
        clientlist.clear()

def recive_message(myserver,b ):
    while True:
        msg = myserver.recv(1024).decode()
        if not msg:
            break
        command = msg.split()[0]

        if command == 'im_online':
            _ , name = msg.split()
            msg =f'{name} {b[0]}' # name ip
            if msg not in clientlist:
                clientlist.append(msg)
                #print(f'-------------->{clientlist}')
        elif command == 'get_list':
            print(clientlist)
            myserver.send(f'{clientlist}'.encode())
        elif command == 'dice':
            myserver.send(f'{random.randint(1,6)}'.encode())



clientlist = []
server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0',2223))
server.listen(10)
print(f'server is listenning on ')
my2thread = threading.Thread(target=clear_online_clients)
my2thread.start()
while True:

    a , b = server.accept()

    my1thread = threading.Thread(target=recive_message,args=(a,b))

    my1thread.start()
    print(f'{b} ooommaaadd')
