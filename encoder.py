import json
import base64
import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def generate_salt() -> bytes:
    return os.urandom(16)

def generate_nonce() -> bytes:
    return os.urandom(12)

def delive_key(passphrase: str, salt: bytes) -> bytes:

    kdf = Scrypt(
        salt = salt,
        length = 32,
        n = 2**14,
        r = 8,
        p = 1,
    )
    return kdf.derive(passphrase.encode("utf-8"))

def encrypt_text(passphrase: str, plaintext: str) -> tuple[bytes, bytes, bytes]:
    salt = generate_salt()
    nonce = generate_nonce()

    key = delive_key(passphrase, salt)
    aesgcm = AESGCM(key)

    ciphertext = aesgcm.encrypt(
        nonce = nonce,
        data = plaintext.encode("utf-8"),
        associated_data = None,
    )

    payload = {
        "v": 1,
        "s": base64.urlsafe_b64encode(salt).decode("ascii"),
        "n": base64.urlsafe_b64encode(nonce).decode("ascii"),
        "c": base64.urlsafe_b64encode(ciphertext).decode("ascii"),
    }

    return json.dumps(payload, ensure_ascii=False, separators=(",",":"))