import socket
import ssl
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

# Load private key
with open("private_key_1.pem", "rb") as key_file:
    private_key = RSA.import_key(key_file.read())

# Create a socket and listen on port 2001
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 2001))
server_socket.listen(5)

print("Listening on port 2001...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Receive the encrypted message
    encrypted_message = client_socket.recv(4096)
    client_socket.close()

    # Decrypt the message
    cipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher_rsa.decrypt(base64.b64decode(encrypted_message))

    # Send the decrypted message to another server
    print(decrypted_message)
    target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target_server_address = os.getenv('TARGET_SERVER_ADDRESS')
    target_server_address = 'router2'
    print(f'target server address: {target_server_address}')
    target_socket.connect((target_server_address, 2001))
    target_socket.sendall(decrypted_message)
    target_socket.close()

    print("Message forwarded to the target server.")