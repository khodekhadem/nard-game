import socket
import ssl
import base64
from Crypto.PublicKey import RSA 
from Crypto.Cipher import PKCS1_OAEP , AES

#AES_KEY = b'This is a key123'

# Padding for the input string --not related to encryption itself.
BLOCK_SIZE = 16
PADDING = '{'

# Function to pad the input string
#def pad(s):
#    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING


# Function to encrypt a message
def encrypt(message, AES_KEY):
    cipher = AES.new(AES_KEY, AES.MODE_ECB)
    encoded = base64.b64encode(cipher.encrypt(pad(message).encode('utf-8')))
    return encoded.decode('utf-8')

# Load public keys
keys = []
for i in range(1, 4):
    with open(f"AES{i}", "rb") as key_file:
        tmp = key_file.read()
        print(f"tmp: {tmp}")
        keys.append(tmp)  # Append tmp directly since it's already bytes

# Encrypt the message with all public keys
message = "Hello, this is a test message."
encrypted_message = message

for key in keys:
    print('log------------------------')
    encrypted_message = encrypt(encrypted_message, key)
    print(f"Encrypted: {encrypted_message}")
    

# Create a socket and connect to the router
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(( 'router1', 2001))

# Send the encrypted messages
client_socket.sendall(str.encode(encrypted_message))

client_socket.close()

print("Encrypted messages sent to the router.")