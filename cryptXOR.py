# /bin/python3
class CryptXOR:
    def encrypt(key, msgclear):
        encryptedMsg = ""
        for indexMsg in range(0, len(msgclear)):
            encryptedMsg += chr(ord(msgclear[indexMsg])^ord(key[indexMsg%len(key)]))
        return encryptedMsg

    def decrypt(key, msgcrypted):
        decryptedMsg = ""
        for indexMsg in range(0, len(msgcrypted)):
            decryptedMsg += chr(ord(msgcrypted[indexMsg])^ord(key[indexMsg%len(key)]))
        return decryptedMsg
