# Password Generator and Encryption

This program is a password generator with options to create passwords using lowercase letters, uppercase letters, numbers, and symbols, only uppercase letters and numbers, or only letters. Additionally, it allows users to enter a custom password.

The generated password can be encrypted using the Caesar Cipher. The program prompts the user to enter a seed for encryption and saves the encrypted passwords to a destination file ('encrypted.txt').

## Functions
- `new_line()`: prints a blank line.
- `line()`: prints a line of '-' characters for readability.
- `decision_menu()`: displays a menu for the user to choose the password type.
- `password_generator(decision)`: generates the password based on the user's choice.
- `encrypt_password(password)`: encrypts the password using the Caesar Cipher.
- `decrypt_password(encrypted_password)`: decrypts the password using the Caesar Cipher.
- `send_to_file(content, destin)`: saves the encrypted password to a destination file.

## Variables
- `min`, `max`, `num`, `sybs`: sets of characters for password generation.
- `all`: set of all characters for complete passwords.
- `MAXnum`: set of characters for passwords with uppercase letters and numbers.
- `MAXmin`: set of characters for passwords with uppercase and lowercase letters.
- `destin_file`: destination file for encrypted passwords.

## Program Flow
The program starts with a loop where the user can choose to generate a password, decrypt a password, or exit. If generating a password, the user selects the platform and length, and then chooses the password type. The password is then encrypted and saved to a file. If decrypting a password, the user enters the encrypted password and seed to decrypt it.

## Clearing the Screen
At the end of the code, the screen is cleared using `os.system('cls')` for Windows and `os.system('clear')` for other operating systems.
