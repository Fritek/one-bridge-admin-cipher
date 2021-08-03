from Crypto.Cipher import AES

key = str.encode("C78857B2C06293AABAA3332A1A80A684")
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce

ciphertext, tag = cipher.encrypt_and_digest(str.encode("interesting"))


cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
try:
    cipher.verify(tag)
    print("The message is authentic:", plaintext)
except ValueError:
    print("Key incorrect or message corrupted")


import secrets

print(secrets.token_urlsafe(16))

print(secrets.token_hex(16))
