# Simple password manager

## Description:
    A small project that helped me understand the basics of Python.
    
## Details:
    The program should be able to store the username and the password
    for a certain site and copy them to the user's clipboard based on the 
    user's choice. The program will work with 4 files:
        - Key.txt:  the key that is used to crypt and decrypt the 
                    passwords/ usernames.

        - MasterPassword.txt:   the password that will be checked for
                                to access the stored in other 
                                info files.

        - Users.txt and Password.txt:   stored two different dictionaries
                                        that will have the following format:
                                        website: encrypted password/
                                        username

    ! The program also keeps backup files in "home/user/Documents"

    ! The password and usernames will be encrypted before storing
