import os
from cryptography.fernet import Fernet
from django.shortcuts import render, redirect, HttpResponseRedirect

def generate_key():
    key = Fernet.generate_key()
    return key

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(data)

    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            encrypt_file(file_path, key)

def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            decrypt_file(file_path, key)

# Generate a random key
# encryption_key = generate_key()
encryption_key = b'0FndrQoOgYDr-q5ezMoHhx3z_TaiAlgDRIZSsAb8lgQ='

# Specify the path to the folder you want to encrypt
# folder_path = '/path/to/your/folder'
folder_path = 'E:\other\MOHSEN\python\simo\simo_dataset\dataset_3'

######################################## main #####################################



def crypto(request, action):

    if action == "encrypt":
        # Encrypt the folder
        # import sys
        # sys.path.append("E:\other\Mohsen\python\.......")
        encrypt_folder(folder_path, encryption_key)

    elif action == "decrypt":
        # Decrypt the folder
        decrypt_folder(folder_path, encryption_key)

    context = {
        "data": "test...OK",
    }
    return render(request, 'index/result.html', context)







# in powershell for run folder with vscode
# code .

# django-admin.exe startproject encrypt_folder_4
# python.exe .\manage.py startapp app_1

# select interpreter for vscode
# ctl + shift + p
