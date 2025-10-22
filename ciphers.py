import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            if mode == 'encrypt':
                shifted = (ord(char) - start + shift) % 26
            else:
                shifted = (ord(char) - start - shift) % 26
            result += chr(start + shifted)
        else:
            result += char
    return result

def vigenere_cipher(text, key, mode='encrypt'):
    result = []
    key = key.lower()
    key_len = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            key_shift = ord(key[i % key_len]) - ord('a')
            shift = key_shift if mode == 'encrypt' else -key_shift
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

def rail_fence_encrypt(text, rails):
    if rails <= 1:
        return text
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    for char in text:
        fence[rail].append(char)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= 1
    return ''.join([''.join(row) for row in fence])


def rail_fence_decrypt(cipher, rails):
    if rails <= 1:
        return cipher
    pattern = list(range(rails)) + list(range(rails - 2, 0, -1))
    cycle = len(pattern)
    n = len(cipher)
    indexes = sorted(range(n), key=lambda i: pattern[i % cycle])
    result = [''] * n
    for i, idx in enumerate(indexes):
        result[idx] = cipher[i]
    return ''.join(result)

def aes_encrypt(text, key):
    key_bytes = key.encode('utf-8')
    if len(key_bytes) not in [16, 24, 32]:
        raise ValueError("AES key must be 16, 24, or 32 bytes long.")
    data_bytes = text.encode('utf-8')
    cipher = AES.new(key_bytes, AES.MODE_CBC)
    iv = cipher.iv
    ct_bytes = cipher.encrypt(pad(data_bytes, AES.block_size))
    return base64.b64encode(iv).decode('utf-8'), base64.b64encode(ct_bytes).decode('utf-8')

def aes_decrypt(iv_b64, ciphertext_b64, key):
    key_bytes = key.encode('utf-8')
    if len(key_bytes) not in [16, 24, 32]:
        raise ValueError("AES key must be 16, 24, or 32 bytes long.")
    iv = base64.b64decode(iv_b64)
    ct = base64.b64decode(ciphertext_b64)
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    pt_bytes = unpad(cipher.decrypt(ct), AES.block_size)
    return pt_bytes.decode('utf-8')

def base64_encode(text):
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')


def base64_decode(text):
    return base64.b64decode(text.encode('utf-8')).decode('utf-8')
def sha256_hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()
