import os

origin_file = "decrypted.txt"

destin_file = "encrypted.txt"


with open(origin_file, 'r') as f:
    password = f.read()


SEED = int(input('Digite a seed: '))

# encrypt the password

def encrypt_password(password):
    """
    Encrypts a password using the Caesar cipher.

    :param password: str - the password to be encrypted.
    :param key: int - the encryption key (default is 3).
    :return: str - the encrypted password.
    """
    encrypted = ''
    for char in password:
        if char.isalpha():
            shifted = chr((ord(char) - 97 + SEED) % 26 + 97)
            encrypted += shifted
        else:
            encrypted += char
    return encrypted

def decrypt_password(encrypted_password):
    """
    Decrypts a password using the Caesar cipher.
    :param password: str - the password to be decrypted.
    :param key: int - the encryption key (default is 3).
    :return: str - the decrypted password.
    """
    decrypted = ''
    for char in encrypted_password:
        if char.isalpha():
            shifted = chr((ord(char) - 97 - SEED) % 26 + 97)
            decrypted += shifted
        else:
            decrypted += char
    return decrypted

encrypt_password = encrypt_password(password)


#send to encrypted.txt
with open(destin_file, 'a') as f:
    f.write(encrypt_password + '\n')
print("Salvo no arquivo encriptado.")