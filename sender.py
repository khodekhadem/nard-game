import socket
import ssl
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Load public keys
public_keys = []
for i in range(1, 3):
    with open(f"public_key_{i}.pem", "rb") as key_file:
        public_keys.append(RSA.import_key(key_file.read()))
for i in public_keys:
    print(i)
    print('------------------')
# Encrypt the message with all public keys
message = b"Hello, this is a test message."
encrypted_messages = []
encrypted_message = message
for public_key in public_keys:
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_message = base64.b64encode(cipher_rsa.encrypt(encrypted_message))

# Create a socket and connect to the router
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(( 'router1', 2001))

# Send the encrypted messages
for encrypted_message in encrypted_messages:
    client_socket.sendall(encrypted_message)

client_socket.close()

print("Encrypted messages sent to the router.")