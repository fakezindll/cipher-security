from cryptography.fernet import Fernet
import base64
import hashlib

# Função para gerar uma chave Fernet válida a partir de qualquer senha
def generate_key_from_password(password: str) -> bytes:
    # Transforma a senha em 32 bytes usando SHA256
    key = hashlib.sha256(password.encode()).digest()
    # Codifica em Base64, formato exigido pelo Fernet
    return base64.urlsafe_b64encode(key)

def encrypt_message(text: str, password: str) -> str:
    key = generate_key_from_password(password)
    cipher = Fernet(key)
    return cipher.encrypt(text.encode()).decode()

def decrypt_message(token: str, password: str) -> str:
    key = generate_key_from_password(password)
    cipher = Fernet(key)
    return cipher.decrypt(token.encode()).decode()
