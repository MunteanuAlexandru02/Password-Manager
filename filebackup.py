import os
import shutil

user = None
absolute_path = None
def get_user():
    global user
    user = input("Please input your user: ")

#   If the files don't exist at the "absolute path"
#   we will create them, otherwise just open and close them
def create_backup_files():
    global absolute_path

    key_file = open(f"{absolute_path}/Key.txt", "wb+")
    master_file = open(f"{absolute_path}/MasterPassword.txt", "wb+")
    password_file = open(f"{absolute_path}/Passwords.txt", "wb+")
    user_file = open(f"{absolute_path}/Users.txt", "wb+")

    key_file.close()
    master_file.close()
    password_file.close()
    user_file.close()

def copy_file(source_file, target_file):

    target_file_size = os.stat(target_file).st_size
    source_file_size = os.stat(source_file).st_size

    if target_file_size < source_file_size:
        shutil.copyfile(source_file, target_file)

def copy_file_inverted(target_file, source_file):
    copy_file(source_file, target_file)

def copy_info_backup_files(function):
    #   Check if the file is empty because we don't want to
    #   overwrite important info
    function("Key.txt", f"{absolute_path}/Key.txt")
    function("MasterPassword.txt", f"{absolute_path}/MasterPassword.txt")
    function("Passwords.txt", f"{absolute_path}/Passwords.txt")
    function("Users.txt",f"{absolute_path}/Users.txt")

def copy_to_backup():
    copy_info_backup_files(copy_file)

def copy_from_backup():
    copy_info_backup_files(copy_file_inverted)

def check_backup(file):
    global absolute_path

    get_user()
    absolute_path = f"/home/{user}/Documents/"

    # If the backup file is empty that means that the key was not set up
    if os.stat(f"/home/{user}/Documents/{file}").st_size == 0:
        return True
    else:
        return False