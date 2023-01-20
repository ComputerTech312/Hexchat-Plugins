import hexchat
import rsa

__module_name__ = "RSA-Chat"
__module_author__ = "ComputerTech"
__module_version__ = "1.0"
__module_description__ = "RSA-Chat: Secure communication in HexChat using RSA encryption."

(pubkey, privkey) = rsa.newkeys(512)

def encrypt_cb(word, word_eol, userdata):
    if len(word) < 2:
        hexchat.prnt("Not enough arguments. Usage: /encrypt message")
        return hexchat.EAT_ALL

    message = word_eol[1]

    encrypted = rsa.encrypt(message.encode(), pubkey)

    hexchat.command("msg {} {}".format(hexchat.get_info("channel"), encrypted))

    return hexchat.EAT_ALL

def decrypt_cb(word, word_eol, userdata):
    if len(word) < 2:
        hexchat.prnt("Not enough arguments. Usage: /decrypt message")
        return hexchat.EAT_ALL

    message = word_eol[1]
    
    decrypted = rsa.decrypt(eval(message), privkey).decode()

    hexchat.prnt("Decrypted message: {}".format(decrypted))

    return hexchat.EAT_ALL


def on_unload(userdata):
    hexchat.prnt("Encryption/Decryption plugin unloaded")

hexchat.hook_command("encrypt", encrypt_cb)
hexchat.hook_command("decrypt", decrypt_cb)
hexchat.hook_unload(on_unload)

hexchat.prnt("Encryption/Decryption plugin loaded.")




