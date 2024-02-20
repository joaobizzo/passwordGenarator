import random
import os

# defining the character sets that can be used to generate the password
min = 'abcdefghijklmnopqrstuvwxyz'
max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
sybs = '[]{}()*#;/,-_%'

# set of characters that can be used to generate complete passwords
all_chars = min + max + num + sybs

# set of characters that can be used to generate passwords with uppercase letters and numbers
max_num = max + num

# set of characters that can be used to generate passwords with uppercase and lowercase letters
max_min = max + min

# name of the file where the encrypted passwords will be saved
destin_file = 'encrypted.txt'

# function to skip a line in the program output
def skip_line():
    print('\n')

# function to print a line in the program output
def print_line():
    print('-' * 50)

# function that displays the menu of options for the user to choose which type of password to generate
def decision_menu():
    print("----PASSWORD TYPES: ----")
    print("[0] - Complete (letters, numbers, symbols)")
    print("[1] - Uppercase letters and numbers")
    print("[2] - Only letters")
    print("[99] - Enter the password")
    skip_line()

# function that generates the password based on the user's choice
def generate_password(decision):
    password = ''
    if decision == '99':
        password = input('Enter the password: ')
    else:
        if decision == '0':
            password =  "".join(random.sample(all_chars, length))
        elif decision == '1':
            password = "".join(random.sample(max_num, length))
        elif decision == '2':
            password = "".join(random.sample(max_min, length))
    print('Password = ' + password)
    password = platform + ' = ' + password
    return password

# function that encrypts the password using the Caesar cipher
def encrypt_password(password):
    """
    Encrypts a password using the Caesar cipher.

    :param password: str - the password to be encrypted.
    :param key: int - the encryption key (default is 3).
    :return: str - the encrypted password.
    """
    # asks the user to enter a seed to encrypt the password
    SEED = int(input('\nEnter a seed to encrypt: '))
    encrypted = ''
    for char in password:
        if char.isalpha():
            shifted = chr((ord(char) - 97 + SEED) % 26 + 97)
            encrypted += shifted
        else:
            encrypted += char
    return encrypted

# function that decrypts the password using the Caesar cipher
def decrypt_password(encrypted_password):
    """
    Decrypts a password using the Caesar cipher.
    :param password: str - the password to be decrypted.
    :param key: int - the encryption key (default is 3).
    :return: str - the decrypted password.
    """
    # asks the user to enter the seed to decrypt the password
    SEED = int(input('Enter the seed to decrypt: '))
    decrypted = ''
    for char in encrypted_password:
        if char.isalpha():
            shifted = chr((ord(char) - 97 - SEED) % 26 + 97)
            decrypted += shifted
        else:
            decrypted += char
    return decrypted

# function to save the encrypted password to a file
def save_to_file(content, destin):
    with open(destin, 'a') as f:
        f.write(content + '\n')
    print(f"File saved successfully in {destin_file}")

# main loop of the program
while True:
    # asking the user if they want to generate a password or exit
    decision = input("Do you want to generate a password? [Y/N] \nDecrypt[99]\nEnter ==> ")
    
    # if the user wants to generate a password
    if decision == 'Y' or decision == 'y':
        # displaying a separator to make the output more readable
        print_line()
        # asking the user for the platform name (e.g., "Gmail")
        platform = input('Platform: ')
        # asking the user for the length of the password they want to generate
        length = int(input('Enter how many characters: '))
        # displaying a menu of options for the user to choose the password type
        decision_menu()
        # asking the user to choose the password type
        decision = input("Enter which type of password: ")
        # generating the password based on the user's decision
        password = generate_password(decision)
        # encrypting the generated password
        encrypted_password = encrypt_password(password)
        # saving the encrypted password to a file
        save_to_file(encrypted_password, destin_file)
        # displaying a separator to make the output more readable
        print_line()
        skip_line()
    # if the user wants to decrypt a password
    elif decision == '99':
        # asking the user for the encrypted password
        decrypted_password = decrypt_password(input('Enter the encrypted password: '))
        skip_line()
        # displaying the decrypted password
        print(f"Decrypted password = {decrypted_password}")
        skip_line()
        # displaying a separator to make the output more readable
        print_line()
    # if the user wants to exit the program
    elif decision == 'N' or decision == 'n':
        break
    # if the user enters an invalid option
    else:
        print("Invalid option, please try again!")

# clearing the screen
os.system('cls' if os.name == 'nt' else 'clear')
