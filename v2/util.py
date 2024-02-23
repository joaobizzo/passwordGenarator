import random

min = 'abcdefghijklmnopqrstuvwxyz'
max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
sybs = '*#$/-%'

# letra maiuscula e minuscula e numeros e simbolos
all = min + max + num + sybs
# letra maiúsculas e números
MAXnum = max + num
# só letras maiúsculas e minúsculas
MAXmin = max + min



def pulaLinha():
    print('\n')


def linha():
    print('-' * 50)


def menu_decisao():
    print("----TIPOS DE SENHA: ----")
    print("[1] - Completo (letras, numeros, simbolos)")
    print("[2] - Letras maiúsculas e números")
    print("[3] - Somente letras")
    print("[4] - Digitar a senha")
    pulaLinha()


def password_generator(decisao):
    linha()
    plataforma = input('Plataforma: ')
    length = int(input('Digite quantos caracteres: '))
    menu_decisao()
    decisao = input("Digite qual tipo de senha: ")
    password = ''
    if decisao == '4':
        password = input('Digite a senha: ')
    else:
        if decisao == '1':
            password =  "".join(random.sample(all, length))
            

        elif decisao == '2':
            password = "".join(random.sample(MAXnum, length))

        elif decisao == '3':
            password = "".join(random.sample(MAXmin, length))
    print('Senha = ' + password)
    password = plataforma + ' = ' + password
    return password


# encrypt the password
def encrypt_password(password):
    """
    Encrypts a password using the Caesar cipher.

    :param password: str - the password to be encrypted.
    :param key: int - the encryption key (default is 3).
    :return: str - the encrypted password.
    """
    SEED = int(input('\nCrie uma seed para encriptografar: '))
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
    SEED = int(input('Digite a seed para desencriptografar: '))
    decrypted = ''
    for char in encrypted_password:
        if char.isalpha():
            shifted = chr((ord(char) - 97 - SEED) % 26 + 97)
            decrypted += shifted
        else:
            decrypted += char
    return decrypted


def send_to_file(content, destin):
    try:
        with open(destin, 'a') as f:
            f.write(content + '\n')
        print(f"Arquivo salvo com sucesso em {destin}")
    except FileNotFoundError:
        print("O arquivo não pôde ser encontrado ou criado.")
    except IOError:
        print("Erro de E/S ao tentar escrever no arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
