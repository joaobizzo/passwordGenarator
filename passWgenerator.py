import random
import os

min = 'abcdefghijklmnopqrstuvwxyz'
max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
sybs = '[]{}()*#;/,-_%'
plataforma = input('Plataforma: ')
qnt = input('Digite qual tamanho da senha: ')
qntInt = int(qnt)
length = qntInt


# letra maiuscula e minuscula e numeros e simbolos
all = min + max + num + sybs
# letra maiúsculas e números
MAXnum = max + num
# só letras maiúsculas e minúsculas
MAXmin = max + min

print("----TIPOS DE SENHA: ----")
print("")
print("[0] - Completo (letras, numeros, simbolos)")
print("[1] - Letras maiúsculas e números")
print("[2] - Somente letras")
print("[99] - Digitar a senha")
print("")

decisao = input("Digite qual tipo de senha: ")

if decisao == '0':
    password = "".join(random.sample(all, length))
    print('password = ' + password)
    
    
elif decisao == '1':
    password = "".join(random.sample(MAXnum, length))
    print('password = ' + password)
    
    
elif decisao == '2':
    password = "".join(random.sample(MAXmin, length))
    print('password = ' + password)
    

elif decisao == '99':
    password = input('Digite a senha: ')
    print('password = ' + password)


#send to decrypted.txt
with open('decrypted.txt', 'a') as f:
    f.write(plataforma + ' = ' + password + '\n')
print("Salvo no arquivo de encrypt!")


# limpar a tela
os.system('cls' if os.name == 'nt' else 'clear')