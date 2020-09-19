import hashlib


def encode(password):
    print(password)
    encoded = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
    return encoded


def decode(password):
    return
