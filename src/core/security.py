'''
from cryptography.fernet import Fernet
import os

class Security:
    def __init__(self):
        self.key = self.generate_key()
        self.cipher = Fernet(self.key)

    def generate_key(self):
        return Fernet.generate_key()

    def encrypt(self, data):
        if isinstance(data, str):
            data = data.encode()
        encrypted_data = self.cipher.encrypt(data)
        return encrypted_data

    def decrypt(self, encrypted_data):
        decrypted_data = self.cipher.decrypt(encrypted_data)
        return decrypted_data.decode()

    def save_key(self, filepath):
        with open(filepath, 'wb') as key_file:
            key_file.write(self.key)

    def load_key(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'rb') as key_file:
                self.key = key_file.read()
                self.cipher = Fernet(self.key)
        else:
            raise FileNotFoundError("Key file not found.")
'''