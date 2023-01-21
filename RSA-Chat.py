import hexchat
import random
import string
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

__module_name__ = "RSA-Chat"
__module_author__ = "ComputerTech"
__module_version__ = "1.0"
__module_description__ = "RSA-Chat: Secure communication in HexChat using RSA encryption."

# Generate a random one-time key code
def generate_key():
    key = Fernet.generate_key()
    return key

# Encrypt a message using the key
def encrypt_message(key, message):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Decrypt a message using the key
def decrypt_message(key, encrypted_message):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# HexChat plugin command to encrypt a message
def encrypt_cmd(word, word_eol, userdata):
    if len(word) < 2:
        hexchat.prnt("Error: Please provide a message to encrypt.")
    else:
        key = generate_key()
        message = word_eol[1]
        encrypted_message = encrypt_message(key, message)
        hexchat.prnt(f"Encrypted message: {encrypted_message.decode()}")
        hexchat.prnt(f"One-time key code: {key.decode()}")

# HexChat plugin command to decrypt a message
def decrypt_cmd(word, word_eol, userdata):
    if len(word) < 2:
        hexchat.prnt("Error: Please provide an encrypted message and key code.")
    else:
        encrypted_message = word[1]
        key = word[2]
        decrypted_message = decrypt_message(key, encrypted_message)
        hexchat.prnt(f"Decrypted message: {decrypted_message}")


def on_unload(userdata):
    hexchat.prnt("Encryption/Decryption plugin unloaded")
    
# Register the plugin commands with HexChat
hexchat.hook_command("encrypt", encrypt_cmd, help="Usage: /encrypt message")
hexchat.hook_command("decrypt", decrypt_cmd, help="Usage: /decrypt encrypted_message key_code")

hexchat.hook_unload(on_unload)

hexchat.prnt("Encryption/Decryption plugin loaded.")
