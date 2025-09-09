from cryptography.fernet import Fernet

key = input("Enter Key : ").strip()
f = Fernet(key.encode())
ciphertext = input("Enter  CipherText : ").strip()
plaintext = f.decrypt(ciphertext.encode(),ttl=60)
print(plaintext.decode())

