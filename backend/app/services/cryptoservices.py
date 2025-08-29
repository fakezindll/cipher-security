from cryptography.fernet import Fernet

key = Fernet.generate_key()

cipher = Fernet(key)

def encrypt_message(text: str) -> str:
    return cipher.encrypt(text.encode()).decode()

def decrypt_message(token: str) -> str:
    return cipher.decrypt(token.encode()).decode()

