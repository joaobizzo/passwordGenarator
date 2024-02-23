import random
import os
from util import *




destin_file = 'encrypted.txt'

#main
while True:
    decisao = int(input("[1]-Gerar senha nova\n[2]-Desencriptografar\n[3]-Sair\n==> "))
    if decisao == 1:
        senha_criptografada = encrypt_password(password_generator(decisao))
        send_to_file(senha_criptografada, destin_file)
        linha()
        pulaLinha()
    elif decisao == 2:
        senha_desencriptografada = decrypt_password(input('==>'))
        pulaLinha()
        print(f"Senha desencriptografada = {senha_desencriptografada}")
        pulaLinha()
        linha()
    elif decisao == 3:
        break
    
    else:
        print("Opção inválida, tente novamente!")



# limpar a tela
os.system('cls' if os.name == 'nt' else 'clear')