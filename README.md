
# Gerador de Senhas e Encriptação
Esse código é um gerador de senhas com opções para criar senhas com letras minúsculas, maiúsculas, números e símbolos, somente letras maiúsculas e números, ou somente letras. Além disso, há uma opção para digitar uma senha personalizada.

A senha gerada pode ser encriptada usando a Cifra de César, um tipo de criptografia que desloca cada letra em um número fixo de posições no alfabeto.

As senhas geradas e encriptadas são salvas em um arquivo de destino ('encrypted.txt').

## Funções
- pulaLinha(): função que imprime uma linha em branco para deixar o código mais legível.
- linha(): função que imprime uma linha de caracteres '-' para deixar o código mais legível.
- menu_decisao(): função que imprime um menu com as opções de tipos de senhas que o usuário pode escolher.
- password_generator(decisao): função que gera a senha com base na opção selecionada pelo usuário.
- encrypt_password(password): função que encripta a senha utilizando a Cifra de César.
- decrypt_password(encrypted_password): função que desencripta a senha utilizando a Cifra de César.
- send_to_file(content, destin): função que salva a senha encriptada em um arquivo de destino.

## Variáveis
- min: string com todas as letras minúsculas do alfabeto.
- max: string com todas as letras maiúsculas do alfabeto.
- num: string com todos os dígitos de 0 a 9.
- sybs: string com alguns símbolos especiais.
- all: string com todas as letras maiúsculas e minúsculas, números e símbolos.
- MAXnum: string com todas as letras maiúsculas e números.
- MAXmin: string com todas as letras maiúsculas.
- destin_file: nome do arquivo de destino onde as senhas encriptadas serão salvas.

## Fluxo do Programa
O programa começa com um loop while onde é perguntado ao usuário se ele deseja gerar uma senha ou desencriptar uma senha.

Se o usuário escolher gerar uma senha, o programa solicita a plataforma e a quantidade de caracteres desejados para a senha. Depois, o menu com as opções de tipos de senhas é exibido. O usuário escolhe uma opção e a senha é gerada. Em seguida, a senha é encriptada com a Cifra de César, com base em uma seed fornecida pelo usuário. Por fim, a senha encriptada é salva no arquivo de destino.

Se o usuário escolher desencriptar uma senha, ele é solicitado a digitar a senha encriptada e a seed utilizada para encriptar a senha. O programa desencripta a senha e a exibe na tela.

Se o usuário escolher sair do programa, o loop while é interrompido e o programa é finalizado.

## Limpar a Tela
No final do código, há uma linha que limpa a tela do terminal, dependendo do sistema operacional utilizado. No Windows, utiliza-se os.system('cls'), enquanto em outros sistemas operacionais utiliza-se os.system('clear').
