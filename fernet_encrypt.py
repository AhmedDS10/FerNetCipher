from cryptography.fernet import Fernet

key = input("Enter Key : ").strip()
f = Fernet(key.encode())
plaintext = input("Enter PlainText : ").strip()
ciphertext = f.encrypt(plaintext.encode())
print(ciphertext.decode())
