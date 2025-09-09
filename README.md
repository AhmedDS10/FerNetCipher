# Fernet Encryption/Decryption Tools

This repository contains three simple Python scripts for working with Fernet encryption, a symmetric encryption method provided by the `cryptography` library.

## Installation

1. **Install Python** (if not already installed):
   - Download from [python.org](https://www.python.org/downloads/)
   - Or use your package manager:
     ```bash
     # Ubuntu/Debian
     sudo apt-get install python3
     
     # macOS with Homebrew
     brew install python
     
     # Windows with Chocolatey
     choco install python
     ```

2. **Install the cryptography library**:
   ```bash
   pip install cryptography
   ```

3. **Download the scripts**:
   - Save the three Python files (`fernet_key.py`, `fernet_encrypt.py`, `fernet_decrypt.py`) to your desired directory

## Usage

### 1. Generate a Key
First, generate an encryption key:

```bash
python fernet_key.py
```

This will output a base64-encoded key. **Save this key securely** as you'll need it for both encryption and decryption.

Example output:
```
k2qY6X7TdJwV1lP8gR3nH0sZ5mB9cF4xWtLvOyEaMbQ=
```

### 2. Encrypt Data
Use the key to encrypt your plaintext:

```bash
python fernet_encrypt.py
```

You'll be prompted for:
- **Key**: Paste the key generated in step 1
- **PlainText**: Enter the text you want to encrypt

The script will output the encrypted ciphertext.

Example:
```
Enter Key : k2qY6X7TdJwV1lP8gR3nH0sZ5mB9cF4xWtLvOyEaMbQ=
Enter PlainText : This is my secret message
gAAAAABmQ6X9z8V7kL2pN1wHjqF5rT3sM8yB4vC6xWtLvOyEaMbQk2qY6X7TdJwV1lP8gR3nH0sZ5mB9cF4xWtLvO==
```

### 3. Decrypt Data
Use the same key to decrypt the ciphertext:

```bash
python fernet_decrypt.py
```

You'll be prompted for:
- **Key**: Paste the same key used for encryption
- **CipherText**: Enter the encrypted text

The script will output the original plaintext (if decrypted within 60 seconds).

Example:
```
Enter Key : k2qY6X7TdJwV1lP8gR3nH0sZ5mB9cF4xWtLvOyEaMbQ=
Enter CipherText : gAAAAABmQ6X9z8V7kL2pN1wHjqF5rT3sM8yB4vC6xWtLvOyEaMbQk2qY6X7TdJwV1lP8gR3nH0sZ5mB9cF4xWtLvO==
This is my secret message
```

## Important Notes

- **Key Security**: The encryption key must be kept secret and secure. Anyone with the key can decrypt your messages.
- **Time-to-Live (TTL)**: The decryption script includes a 60-second TTL. If you try to decrypt after 60 seconds, it will fail as a security measure.
- **Encoding**: All inputs and outputs are handled in UTF-8 encoding.
- **Error Handling**: These are basic scripts and may crash with invalid inputs. For production use, add proper error handling.

## File Descriptions

- `fernet_key.py` - Generates a new Fernet encryption key
- `fernet_encrypt.py` - Encrypts plaintext using a provided key
- `fernet_decrypt.py` - Decrypts ciphertext using the same key (with 60-second TTL)

## Dependencies

- Python 3.6+
- cryptography library (`pip install cryptography`)

## Security Considerations

- Fernet uses AES-128 in CBC mode with PKCS7 padding
- HMAC with SHA256 is used for authentication
- Includes timestamp to prevent replay attacks within the TTL window
- Suitable for short-lived secrets and messages
