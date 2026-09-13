# lumpo_stdlib/crypto.py
import hashlib
import uuid
import secrets

def sha256(text):
    return hashlib.sha256(str(text).encode('utf-8')).hexdigest()

def md5(text):
    return hashlib.md5(str(text).encode('utf-8')).hexdigest()

def random_uuid():
    return str(uuid.uuid4())

def random_hex(bytes_len=16):
    return secrets.token_hex(bytes_len)
