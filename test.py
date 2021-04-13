# /bin/python3
# Only Ascii char. UTF-8 non supported.
from cryptXOR import CryptXOR

key = "La clef c'est la connaissance."
textclear = "Bonjour je m'appelle Charles."

cryptedTxt = CryptXOR.encrypt(key, textclear)
print(cryptedTxt)
print(CryptXOR.decrypt(key, cryptedTxt))
