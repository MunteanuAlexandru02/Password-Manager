import os

from cryptography.fernet import Fernet
import pickle
import pyperclip

account = None
dictionary = {}

# a dictionary where we can store the username from a site
user_dictionary = {}

def populate_dictionary():
    global dictionary

    file_name = "Passwords.txt"

    if os.stat(file_name).st_size == 0:
        return

    with open(file_name, 'rb') as file:
        dictionary = pickle.load(file)

def populate_user_dictionary():
    global user_dictionary

    file_name = "Users.txt"

    if os.stat(file_name).st_size == 0:
        return

    with open(file_name, 'rb') as file:
        user_dictionary = pickle.load(file)

def encrypt_pass(password, enc_key):
    result = bytes(password, 'utf-8')
    f = Fernet(enc_key)
    token = f.encrypt(result)
    return token

def decrypt_pass(password, enc_key):
    f = Fernet(enc_key)
    token = f.decrypt(password)
    return token

def add_pass_to_file():
    password = input("Please, introduce your password ")

    key_file = open("Key.txt", "rb+")
    key = key_file.read()

    encrypted_password = encrypt_pass(password, key)

    dictionary[account] = encrypted_password

    file_name = "Passwords.txt"

    with open(file_name, 'wb') as file:
        pickle.dump(dictionary, file)

def add_user_to_file():
    user = input("Please, input your username: ")

    key_file = open("Key.txt", "rb+")

    key = key_file.read()

    encrypted_user = encrypt_pass(user, key)

    user_dictionary[account] = encrypted_user

    file_name = "Users.txt"

    with open(file_name, 'wb') as file:
        pickle.dump(user_dictionary, file)

def copy_pass_to_clipboard(key):
    decoded_pass = decrypt_pass(dictionary.get(account), key).decode('utf-8')

    pyperclip.copy(decoded_pass)
    clipboard_content = pyperclip.paste()

def copy_user_to_clipboard(key):
    decoded_user = decrypt_pass(user_dictionary.get(account), key).decode('utf-8')

    pyperclip.copy(decoded_user)
    clipboard_content = pyperclip.paste()
def store_pass():
    global account

    while True:
        account = input("Please type your platform in order to access your password or exit: ")

        if account == "exit":
            exit(0)

        populate_dictionary()
        populate_user_dictionary()

        if dictionary.get(account) == None:
            print("Looks like you don't have a username/password stored for this account.")
            response = input("Would you like to store it (Yes/No)? ")

            if response == "No" or response == "no":
                exit(1)
            elif response == "Yes" or response == "yes":
                add_pass_to_file()
                add_user_to_file()
        else:
            print("User Found!")
            key_file = open("Key.txt", "rb+")
            key = key_file.read()

            while True:
                response = input("Please, choose between username/password/exit: ")

                if response == "password":
                    print("Copying password to clipboard...")
                    copy_pass_to_clipboard(key)
                elif response == "username":
                    print("Copying username to clipboard...")
                    copy_user_to_clipboard(key)
                else:
                    break