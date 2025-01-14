import socket
import os
import threading
from multiprocessing import Process
import time
import sys
import sender
import chat as webchat
import multiprocessing


def game_server_bind_accept():
    global voroodi_available
    global loop_available
    global game_server_bind 
    game_server_bind_conn , game_server_bind_addr = game_server_bind.accept()

    voroodi_available = False
    loop_available = False
    #os.system('clear')
    print('you have message press enter two times to open the message')
    input()
    gameok = input('do you want to play? yes/no \n')
    #send some thing to stdout  

    game_server_bind_conn.sendall(gameok.encode())
    if gameok == 'yes':
        print(f'recived message is {game_server_bind_conn.recv(1024).decode()}')
        print('open the game on the browser')
        print(f'{game_server_bind_conn.recv(1024).decode()}')
        #game_server_bind_conn.shutdown(socket.SHUT_RDWR)
        #game_server_bind_conn.close()
        #game_server_bind.shutdown(socket.SHUT_RDWR)
        #game_server_bind.close()
        #game_server_bind_conn.close()
        #game_server_bind.close()
    else:
        #game_server_bind_conn.close()
        #game_server_bind.close()
        print(f'status {gameok}')
        main()


def send_message(msg,myserver):
    #myserver.send(f'{msg}'.encode())
    sender.start(msg,myserver,'router1')

    #print('sent')
def send_loop_message(msg,delay=0):
    while loop_available:
        #print(f' available {loop_available}')
        if delay>0:
            time.sleep(delay)
        send_message(msg,server)
def star_webchat():
    webchat.start()
def game(ip):
    global voroodi_available
    global loop_available
    voroodi_available = False
    loop_available = False

    game_server_connect =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    game_server_connect.connect((ip,8888))
    # send_message('man omadam bazi',game_server_connect)
    webchat_process = multiprocessing.Process(target=star_webchat)
    webchat_process.start()
    #print the first args gave when call the python file 
    game_server_connect.sendall(f'hi im {sys.argv[1]} lets play!'.encode())
    gameok = game_server_connect.recv(1024).decode()
    if gameok == 'yes':
        #game_server_bind.close()
        game_server_connect.sendall(f'{socket.gethostbyname(socket.gethostname())}:5000'.encode())
    else:
        print('game is not ok')
        webchat_process.terminate()
        return

    print(f'recived message is {gameok}')
    
    chat_list=[]
    #while True:
    #    time.sleep(1)
    #    print('game wait' )
    

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
        if not inp:
            continue
        elif inp == '1':
            os.system('clear')
            #print('im in one')
            send_message('get_list',server)
            print(server.recv(1024).decode())
        elif inp=='2':
            loop_available= True
            send_online=threading.Thread(target=send_loop_message,args=(f'im_online {sys.argv[1]} {socket.gethostbyname(socket.gethostname())}',1))
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
        else:
            True
        


voroodi_available = None
loop_available = None
server = None
game_server_bind = None

def main():
    if len(sys.argv) < 2:
        print('please enter your name  python3 client.py {name}')
        exit()
    global voroodi_available 
    global loop_available
    global server
    global game_server_bind 
    try:
        game_server_bind.close()
    except:
        True


    voroodi_available = True
    loop_available=True

    server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #server.connect(('127.0.0.1',2223))


    #server.connect(('server',2223))

    game_server_bind=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    game_server_bind.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    game_server_bind.bind(('0.0.0.0',8888))
    game_server_bind.listen(1)




    voroodi_thread=threading.Thread(target=vorodi)
    voroodi_thread.start()
    #voroodi_thread=Process(target=vorodi)
    #voroodi_thread.start()

    game_server_bind_thread=threading.Thread(target=game_server_bind_accept)
    game_server_bind_thread.start()

if __name__ == '__main__':
    main()