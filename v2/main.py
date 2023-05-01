# WINDOWS VERSION

import random
import os

# definindo os conjuntos de caracteres que podem ser utilizados para gerar a senha
min = 'abcdefghijklmnopqrstuvwxyz'
max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
sybs = '[]{}()*#;/,-_%'

# conjunto de caracteres que pode ser utilizado para gerar senhas completas
all = min + max + num + sybs

# conjunto de caracteres que pode ser utilizado para gerar senhas com letras maiúsculas e números
MAXnum = max + num

# conjunto de caracteres que pode ser utilizado para gerar senhas com letras maiúsculas e minúsculas
MAXmin = max + min

# nome do arquivo onde as senhas criptografadas serão salvas
destin_file = 'encrypted.txt'

# função para pular uma linha na saída do programa
def pulaLinha():
    print('\n')

# função para imprimir uma linha na saída do programa
def linha():
    print('-' * 50)

# função que mostra o menu de opções para o usuário escolher qual tipo de senha deseja gerar
def menu_decisao():
    print("----TIPOS DE SENHA: ----")
    print("[0] - Completo (letras, numeros, simbolos)")
    print("[1] - Letras maiúsculas e números")
    print("[2] - Somente letras")
    print("[99] - Digitar a senha")
    pulaLinha()

# função que gera a senha com base na opção escolhida pelo usuário
def password_generator(decisao):
    password = ''
    if decisao == '99':
        password = input('Digite a senha: ')
    else:
        if decisao == '0':
            password =  "".join(random.sample(all, length))
        elif decisao == '1':
            password = "".join(random.sample(MAXnum, length))
        elif decisao == '2':
            password = "".join(random.sample(MAXmin, length))
    print('Senha = ' + password)
    password = plataforma + ' = ' + password
    return password

# função que encriptografa a senha usando o cifra de César
def encrypt_password(password):
    """
    Encrypts a password using the Caesar cipher.

    :param password: str - the password to be encrypted.
    :param key: int - the encryption key (default is 3).
    :return: str - the encrypted password.
    """
    # solicita que o usuário digite uma seed para encriptar a senha
    SEED = int(input('\nCrie uma seed para encriptografar: '))
    encrypted = ''
    for char in password:
        if char.isalpha():
            shifted = chr((ord(char) - 97 + SEED) % 26 + 97)
            encrypted += shifted
        else:
            encrypted += char
    return encrypted

# função que desencriptografa a senha usando o cifra de César
def decrypt_password(encrypted_password):
    """
    Decrypts a password using the Caesar cipher.
    :param password: str - the password to be decrypted.
    :param key: int - the encryption key (default is 3).
    :return: str - the decrypted password.
    """
    # solicita que o usuário digite a seed para desencriptar a senha
    SEED = int(input('Digite a seed para desencriptografar: '))
    decrypted = ''
    for char in encrypted_password:
        if char.isalpha():
            shifted = chr((ord(char) - 97 - SEED) % 26 + 97)
            decrypted += shifted
        else:
            decrypted += char
    return decrypted
    # função para salvar a senha criptografada em um arquivo
def send_to_file(content, destin):
    with open(destin, 'a') as f:
        f.write(content + '\n')
    print(f"Arquivo salvo com sucesso em {destin_file}")

# loop principal do programa
while True:
    # perguntando ao usuário se ele quer gerar uma senha ou sair
    decisao = input("Deseja gerar senha? [S/N] \nDesencriptografar[99]\nDigite ==> ")
    
    # se o usuário quiser gerar uma senha
    if decisao == 'S' or decisao == 's':
        # exibindo um separador para tornar a saída mais legível
        linha()
        # pedindo ao usuário o nome da plataforma (por exemplo, "Gmail")
        plataforma = input('Plataforma: ')
        # pedindo ao usuário o comprimento da senha que ele quer gerar
        length = int(input('Digite quantos caracteres: '))
        # exibindo um menu de opções para o usuário escolher o tipo de senha
        menu_decisao()
        # pedindo ao usuário para escolher o tipo de senha
        decisao = input("Digite qual tipo de senha: ")
        # gerando a senha com base na decisão do usuário
        senha = password_generator(decisao)
        # criptografando a senha gerada
        senha_criptografada = encrypt_password(senha)
        # salvando a senha criptografada em um arquivo
        send_to_file(senha_criptografada, destin_file)
        # exibindo um separador para tornar a saída mais legível
        linha()
        pulaLinha()
    # se o usuário quiser descriptografar uma senha
    elif decisao == '99':
        # pedindo ao usuário a senha criptografada
        senha_desencriptografada = decrypt_password(input('Digite a senha criptografada: '))
        pulaLinha()
        # exibindo a senha descriptografada
        print(f"Senha desencriptografada = {senha_desencriptografada}")
        pulaLinha()
        # exibindo um separador para tornar a saída mais legível
        linha()
    # se o usuário quiser sair do programa
    elif decisao == 'N' or decisao == 'n':
        break
    # se o usuário inserir uma opção inválida
    else:
        print("Opção inválida, tente novamente!")

# limpando a tela
os.system('cls' if os.name == 'nt' else 'clear')


# FOR LINUX:
