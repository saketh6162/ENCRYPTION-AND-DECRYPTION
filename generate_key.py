from cryptography.fernet import Fernet

def generate_key():
    """Generates and saves an encryption key."""
    key = Fernet.generate_key()  # Generates a 32-byte key
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

    print("✅ Encryption key generated and saved in 'secret.key'.")

# Run the function when script is executed
if __name__ == "__main__":
    generate_key()
