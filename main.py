from filebackup import *
from store_passwords import *
import os
def set_up_master_pass():
    password = input("Please choose your master password: ")
    return password

def print_error_file():
    print("The file doesn't exist or couldn't be opened.")
    exit(1)

def compare_pass(file_pass, user_pass):
    result = bytes(user_pass, 'utf-8')
    return result == file_pass

#   if a file can't be opened, we will try to access
#   the backup file stored somewhere in the computer
try:
    key_file = open("Key.txt", "rb+")
except:
    print_error_file()

# Check if there is an encrytion key
key = None
if os.stat("Key.txt").st_size == 0 and check_backup("Key.txt"):
    key = Fernet.generate_key()
    key_file.write(key)
elif os.stat("Key.txt").st_size != 0:
    key = key_file.read()
# The backup file is not empty
elif os.stat("Key.txt").st_size == 0 and check_backup("Key.txt") == False:
    copy_from_backup()
    key = key_file.read()

master_password = None
number_of_bytes = os.stat("MasterPassword.txt").st_size

try:
    master_file = open("MasterPassword.txt", "rb+")
except:
    print_error_file()

if number_of_bytes == 0 and check_backup("MasterPassword.txt"):
    print('Looks like you have not yet set your master password.')
    response = input('Would you like to set it now (Yes/No)? ')
    if response == "No" or response == "no":
        exit(0)
    elif response == "Yes" or response == "yes":
        master_password = set_up_master_pass()
        token = encrypt_pass(master_password, key)
        master_file.write(token)
    else:
        exit(1)
elif number_of_bytes == 0 and check_backup("MasterPassword.txt") == False:
    copy_from_backup()

master_password = input("Please, insert your master password in order to access your information: ")
to_compare_pass = master_file.read()

to_compare_pass = decrypt_pass(to_compare_pass, key)

if compare_pass(to_compare_pass, master_password):
    print("Welcome!")
    store_pass()
else:
    print("Master password does not match!")
    exit(1)