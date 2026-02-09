from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import hashlib

def aes_ecb_encrypt(key, data):
    return AES.new(key, AES.MODE_ECB).encrypt(pad(data, 16))

def aes_cbc_encrypt(key, iv, data):
    return AES.new(key, AES.MODE_CBC, iv).encrypt(pad(data, 16))

def sha256(x):
    return hashlib.sha256(x).digest()

