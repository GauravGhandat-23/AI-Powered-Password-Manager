<h1 align="center"> 🛡️ AI-Powered Password Manager 🛡️ </h1>


![AI-Powered Password Manager](https://img.shields.io/badge/AI%2DPowered%20Password%20Manager-blue?style=for-the-badge&logo=security)

## ![Overview](https://img.shields.io/badge/Overview-📖-blue?style=for-the-badge)

Welcome to the **AI-Powered Password Manager**! This is a simple, secure, and efficient way to store your passwords. Built using **Streamlit**, **SQLite**, and **Fernet encryption**, this app ensures that your passwords are safe and easily accessible.

## ![Features](https://img.shields.io/badge/Features-✨-green?style=for-the-badge)

- **Add Passwords**: Securely add your passwords for various services.
- **View Passwords**: View stored passwords with automatic decryption (passwords are encrypted before storage).
- **Delete Passwords**: Remove entries from the database as needed.
- **AES Encryption**: Uses **Fernet** encryption to ensure your passwords are securely stored.

## ![Tech Stack](https://img.shields.io/badge/Tech%20Stack-🖥️-blue?style=for-the-badge)

- **Streamlit**: Web application framework for building the interface.
- **SQLite**: Lightweight database to store user passwords.
- **Cryptography**: AES-like encryption (Fernet) for securely storing passwords.

## ![Setup Instructions](https://img.shields.io/badge/Setup%20Instructions-⚙️-yellow?style=for-the-badge)

To get started, follow these steps:

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/password-manager.git
   cd password-manager

2. **Install Dependencies**
- Ensure you have Python 3.8+ installed, then install the necessary libraries:
  
   ```bash
   pip install -r requirements.txt

3. **Run the App**
- Start the application with:

   ```bash
   streamlit run app.py
- Once the app is running, open your browser and go to http://localhost:8501 to start using the password manager.

## ![How It Works](https://img.shields.io/badge/How%20It%20Works-🔧-purple?style=for-the-badge)

1. **Add Passwords**:
- Input the service name, username, and password.
- Your password is encrypted before being stored in the database.

![test 1](https://github.com/user-attachments/assets/d97a9318-80a4-4295-95ad-d68b09fa9f1f)

2. **View Passwords**:
- Retrieve and decrypt your saved passwords for viewing.

![test 2](https://github.com/user-attachments/assets/d01614cb-02c2-4662-86a2-7a10686d294c)

3. **Delete Passwords**:
- Delete saved password entries when they are no longer needed.

## ![Security](https://img.shields.io/badge/Security-🔒-red?style=for-the-badge)

- The password manager uses Fernet encryption to ensure the security of your passwords. Your encryption key is stored in a file called secret.key. Keep this key safe! If the key is lost or compromised, the stored passwords will be at risk.

## ![Encryption Process](https://img.shields.io/badge/Encryption%20Process-🔑-orange?style=for-the-badge)

- Passwords are encrypted before being saved in the database.
- The decryption process occurs when you want to view your saved passwords.

## 🤝 Contributing
- We welcome contributions! If you would like to improve or add new features to this project, please fork the repository and submit a pull request.

## Connect with Me 🌐

- 📧 [Email](mailto:gauravghandat12@gmail.com)
- 💼 [LinkedIn](www.linkedin.com/in/gaurav-ghandat-68a5a22b4)























 





   
    
