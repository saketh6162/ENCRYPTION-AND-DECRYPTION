from cryptography.fernet import Fernet
import sys

# Function to load the saved encryption key
def load_key():
    """Loads the encryption key from a file."""
    return open("secret.key", "rb").read()

# Function to encrypt a file
def encrypt_file(filename):
    """Encrypts a file using AES encryption."""
    key = load_key()
    cipher = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = cipher.encrypt(file_data)

    with open(filename + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"✅ File '{filename}' has been encrypted as '{filename}.enc'.")

# Function to decrypt a file
def decrypt_file(encrypted_filename):
    """Decrypts an encrypted file using AES."""
    key = load_key()
    cipher = Fernet(key)

    with open(encrypted_filename, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    original_filename = encrypted_filename.replace(".enc", "")

    with open(original_filename, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"🔓 File '{encrypted_filename}' has been decrypted back to '{original_filename}'.")

# Command-line Interface for users
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("🔒 Encrypt: python encrypt_decrypt.py encrypt <filename>")
        print("🔓 Decrypt: python encrypt_decrypt.py decrypt <filename.enc>")
        sys.exit(1)

    action = sys.argv[1].lower()
    filename = sys.argv[2]

    if action == "encrypt":
        encrypt_file(filename)
    elif action == "decrypt":
        decrypt_file(filename)
    else:
        print("❌ Invalid action. Use 'encrypt' or 'decrypt'.")
