from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

import hashlib
import os


def get_key(password):
    salt = b'\x9b\x19\x8f\x88\x10\xae\x04\xae' 
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


master_pwd = input("Enter Master Password: ")

attempt_hash = hashlib.sha256(master_pwd.encode()).hexdigest()

if not os.path.exists("master.pass"):
   
    with open("master.pass", "w") as f:
        f.write(attempt_hash)
    print("Master password set!")
else:
  
    with open("master.pass", "r") as f:
        saved_hash = f.read()
    
    if attempt_hash != saved_hash:
        print("❌ Invalid Master Password! Access Denied.")
        exit()
    else:
        print("✅ Access Granted.")


key = get_key(master_pwd)
fer = Fernet(key)




def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                if "|" not in data:
                    continue
                
                user, passw = data.split("|")
                print("User:", user, "| Password:",
                      fer.decrypt(passw.encode()).decode())
    except FileNotFoundError:
        print("No passwords found. Add one first!")

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue