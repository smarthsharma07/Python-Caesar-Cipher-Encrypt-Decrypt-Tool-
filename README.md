# Caesar Cipher — Python Implementation

A clean and minimal Python implementation of the classic Caesar Cipher.  
Uses `str.maketrans()` and `translate()` for efficient character mapping,  
supporting both encryption and decryption for uppercase and lowercase letters.



---

## 🔧 Features
- Encrypt and decrypt text using a shift of 1–25  
- Supports both uppercase and lowercase letters  
- Uses Python’s `str.maketrans` for fast character translation  
- Simple `encrypt()` and `decrypt()` wrapper functions  
- Raises proper exceptions for invalid input  

---

## 🧠 Usage

```python
from caesar import encrypt, decrypt

# Encrypt
cipher_text = encrypt("Hello World", 5)
print(cipher_text)   # Mjqqt Btwqi

# Decrypt
plain_text = decrypt(cipher_text, 5)
print(plain_text)    # Hello World
