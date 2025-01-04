import socket
import os
import threading
from multiprocessing import Process
import time
import sys
import sender

voroodi_available = True
loop_available=True

server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#server.connect(('127.0.0.1',2223))


#server.connect(('server',2223))

game_server_bind=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
game_server_bind.bind(('0.0.0.0',8888))
game_server_bind.listen(1)


def game_server_bind_accept():
    game_server_bind_conn , game_server_bind_addr = game_server_bind.accept()
    global voroodi_available
    global loop_available
    voroodi_available = False
    loop_available = False
    print('game oommmmmmmmaaaaaaaaadddddddddd')
    chat_list=[]
    def printer():
        while True:
            input_msg = game_server_bind_conn.recv(1024).decode()
            chat_list.append(f'{game_server_bind_addr[0]}: {input_msg}')
            os.system('clear')
            for msg in chat_list[-10:]:
                print(msg)
            #time.sleep(2)
    ahay =0
    while True:

        #input_msg = game_server_bind_conn.recv(1024).decode()
        #chat_list.append(f'{game_server_bind_addr[0]}: {input_msg}')
        #print(chat_list[-1])
        
        # Get user input from the console
        user_input = input("Enter message to send: ")
        
        # Send the user input through the socket
        chat_list.append(f'{sys.argv[1]}: {user_input}')
        #game_server_bind_conn.send(user_input.encode())
        if ahay==0:
            ahay=1
            threading.Thread(target=printer).start()


def send_message(msg,myserver):
    #myserver.send(f'{msg}'.encode())
    sender.start(msg)

    #print('sent')
def send_loop_message(msg,delay=0):
    while loop_available:
        #print(f' available {loop_available}')
        if delay>0:
            time.sleep(delay)
        send_message(msg,server)
def game(ip):
    global voroodi_available
    global loop_available
    voroodi_available = False
    loop_available = False
    game_server_bind.close()

    game_server_connect =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    game_server_connect.connect((ip,8888))
    send_message('man omadam bazi',game_server_connect)
    chat_list=[]
    while True:
        os.system('clear')
        for msg in chat_list:
            print(msg)
        input_msg = input()
        chat_list.append(f'{sys.argv[1]}: {input_msg}')
        send_message(input_msg,game_server_connect)
    

def vorodi():
    global loop_available 
    while voroodi_available:
        inp = input("""
        1---get list
        2---online
        3---offline
        4---connect_to {ip}
        """)
        os.system('clear')

        if inp == '1':
            send_message('get_list',server)
            print(server.recv(1024).decode())
        elif inp=='2':
            loop_available= True
            send_online=threading.Thread(target=send_loop_message,args=(f'im_online {sys.argv[1]}',4))
            send_online.start()
        elif inp=='3':
            #send_online.terminate()
            loop_available= False
        elif inp.split()[0]=='4' :
            try:
                ip = inp.split()[1]
                mygame=threading.Thread(target=game,args=(ip,))
                mygame.start()
                # global voroodi_available
                # voroodi_available = False
                break
            except:
                print('please enter 4 {ip address}')
        


if len(sys.argv) < 2:
    print('please enter your name  python3 client.py {name}')
    exit()

voroodi_thread=threading.Thread(target=vorodi)
voroodi_thread.start()
#voroodi_thread=Process(target=vorodi)
#voroodi_thread.start()

game_server_bind_thread=threading.Thread(target=game_server_bind_accept)
game_server_bind_thread.start()
