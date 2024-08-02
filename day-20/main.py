"""
Day 20 - Fernet Encrypt & Decrypt
"""

import click
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    print(f"Encrypted: {encrypted_message}")
    return encrypted_message

def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    print(f"Decrypted: {decrypted_message}")
    return decrypted_message

@click.group()
def cli():
    pass

@click.command()
@click.argument('text')
def encrypt(text):
    """Encrypt text to fernet key."""
    generate_key()
    encrypt_text = encrypt_message(text)
    
@click.command()
@click.argument('encrypted_text')
def decrypt(encrypted_text):
    """Decrypt fernet key to text."""
    decrypt_message(encrypted_text)
    
cli.add_command(encrypt)
cli.add_command(decrypt)

if __name__ == "__main__":
    cli()