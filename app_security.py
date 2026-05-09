import streamlit as st
import pandas as pd
import os
import string
import random
from cryptography.fernet import Fernet
import hashlib
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

st.set_page_config(page_title="Enterprise Security Suite", page_icon="🔐")
st.title("🔐 Enterprise Security Suite")

tab1, tab2 = st.tabs(["Password Generator", "Vault Manager"])


with tab1:
    st.header("Secure Password Generator")
    
    length = st.slider("Select Password Length", 8, 32, 16)
    use_digits = st.checkbox("Include Numbers (0-9)", value=True)
    use_special = st.checkbox("Include Symbols (!@#$)", value=True)

    if st.button("Generate Secure Password"):
        chars = string.ascii_letters
        if use_digits: chars += string.digits
        if use_special: chars += string.punctuation
        
        
        while True:
            pwd = ''.join(random.choice(chars) for _ in range(length))
            if (not use_digits or any(c.isdigit() for c in pwd)) and \
               (not use_special or any(c in string.punctuation for c in pwd)):
                break
        
        st.success("Password Generated Successfully!")
        st.code(pwd) 


with tab2:
    st.header("Encrypted Vault")
    
    
    def get_key(password):
        salt = b'\x9f\x18\x8f\x8c\x8e\x1c\x1e\x1c' 
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    master_pwd = st.text_input("Enter Master Password to Unlock", type="password")

    if master_pwd:
        key = get_key(master_pwd)
        fer = Fernet(key)
        
        action = st.radio("What would you like to do?", ["View Saved Passwords", "Add New Credential"])
        
        if action == "Add New Credential":
            site = st.text_input("Account Name (e.g., Gmail)")
            acc_pwd = st.text_input("Password", type="password")
            
            if st.button("Encrypt and Save"):
                encrypted_pwd = fer.encrypt(acc_pwd.encode()).decode()
                with open("passwords.txt", "a") as f:
                    f.write(f"{site} | {encrypted_pwd}\n")
                st.success(f"Credential for {site} secured!")

        elif action == "View Saved Passwords":
            if st.button("Decrypt Vault"):
                if os.path.exists("passwords.txt"):
                    with open("passwords.txt", "r") as f:
                        for line in f:
                            data = line.strip().split(" | ")
                            if len(data) == 2:
                                site, encrypted = data
                                try:
                                    decrypted = fer.decrypt(encrypted.encode()).decode()
                                    st.text(f"📍 {site}: {decrypted}")
                                except:
                                    st.error("Invalid Master Password for this entry.")
                else:
                    st.info("Vault is currently empty.")