import socket
import ssl
import threading
import base64
from Crypto.PublicKey import RSA 
from Crypto.Cipher import PKCS1_OAEP, AES
import os
# Fixed AES key (must be 16, 24, or 32 bytes long)
#AES_KEY = b'This is a key123'

# Padding for the input string --not related to encryption itself.
BLOCK_SIZE = 16
PADDING = '{'

# Function to pad the input string
def pad(s):
    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

# Function to decrypt a message
def decrypt(encrypted_message,AES_KEY):
    cipher = AES.new(AES_KEY, AES.MODE_ECB)
    decoded = cipher.decrypt(base64.b64decode(encrypted_message)).decode('utf-8')
    return decoded.rstrip(PADDING)

# Load private key
#get AES_NUM from environment variable
AES_NUM = os.getenv('AES_NUM')
print(f"AES_NUM: {AES_NUM}")
with open(f"AES{AES_NUM}", "rb") as key_file:
    key = key_file.read()
    print(f"key: {key}")





# Create a socket and listen on port 2001
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 2001))
server_socket.listen(5)


def baraks(client_socket, target_socket):
    while True:
        back_message = target_socket.recv(4096)
        print(back_message)
        print(type(back_message))
        decrypted_message = decrypt(back_message,key)
        print(decrypted_message)
        print(type(decrypted_message))
        client_socket.sendall(str.encode(decrypted_message))
        print('baraks')
#mythread = threading.Thread(target=baraks)
#mythread.start()

def mostaghim (client_socket, target_socket):
    while True:

        # Receive the encrypted message
        encrypted_message = client_socket.recv(4096)
        #client_socket.close()

        # Decrypt the message
        print(encrypted_message)
        decrypted_message = decrypt(encrypted_message,key)

        # Send the decrypted message to another server
        print(decrypted_message)
        #if AES_NUM == '1':
        #    print(decrypted_message)
        #    break

        print(decrypted_message)
        target_socket.sendall(str.encode(decrypted_message))
        #target_socket.close()

        print("Message forwarded to the target server.")
while True:
    print("Listening on port 2001...")

    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target_server_address = os.getenv('TARGET_SERVER_ADDRESS')
    print(f'target server address:{target_server_address}')
    target_socket.connect((target_server_address, 2001))
    #threading.Thread(target=mostaghim).start()
    mythread = threading.Thread(target=mostaghim, args=(client_socket, target_socket))
    mythread.start()
    mysthread = threading.Thread(target=baraks, args=(client_socket, target_socket))
    mysthread.start()