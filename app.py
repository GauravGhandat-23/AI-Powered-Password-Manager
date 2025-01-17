import streamlit as st
from cryptography.fernet import Fernet
import sqlite3

# Initialize database
DB_NAME = "password_manager.db"
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords (
                 id INTEGER PRIMARY KEY,
                 service TEXT NOT NULL,
                 username TEXT NOT NULL,
                 password TEXT NOT NULL
                 )''')
    conn.commit()
    conn.close()

# Generate encryption key and save it securely
KEY_FILE = "secret.key"
def load_or_create_key():
    try:
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        return key

def encrypt_password(key, password):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(password.encode()).decode()

def decrypt_password(key, encrypted_password):
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(encrypted_password.encode()).decode()

def add_password(service, username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)",
              (service, username, password))
    conn.commit()
    conn.close()

def get_passwords():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT id, service, username, password FROM passwords")
    rows = c.fetchall()
    conn.close()
    return rows

def delete_password(entry_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM passwords WHERE id = ?", (entry_id,))
    conn.commit()
    conn.close()

# Streamlit app
st.title("AI-Powered Password Manager")

# Load or create encryption key
key = load_or_create_key()

# Initialize database
init_db()

# App pages
menu = ["Add Password", "View Passwords"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Password":
    st.subheader("Add a New Password")
    service = st.text_input("Service Name")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Add"):
        encrypted_password = encrypt_password(key, password)
        add_password(service, username, encrypted_password)
        st.success(f"Password for {service} added successfully!")

elif choice == "View Passwords":
    st.subheader("Saved Passwords")
    passwords = get_passwords()

    if passwords:
        for entry in passwords:
            entry_id, service, username, encrypted_password = entry
            decrypted_password = decrypt_password(key, encrypted_password)
            with st.expander(service):
                st.write(f"**Username:** {username}")
                st.write(f"**Password:** {decrypted_password}")
                if st.button("Delete", key=entry_id):
                    delete_password(entry_id)
                    st.success(f"Deleted entry for {service}")
    else:
        st.info("No passwords saved yet.")

st.sidebar.info("Secure Password Manager with AES encryption")
