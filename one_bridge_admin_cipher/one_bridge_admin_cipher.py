from base64 import b64encode, b64decode, urlsafe_b64encode, urlsafe_b64decode
import json
import hashlib
import secrets
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes


class OBACipher:
    def __init__(self, encrptyion_secret_key):
        """
        Initializes One Bridge Admin Cipher with encrptyion_secret_key.

        Parameters
        ----------
        encrptyion_secret_key
            OBACipher encryption secret key.

        """
        self.encrptyion_secret_key = encrptyion_secret_key

    def generate_keys(self):
        """
        Generates OneBridge Admin Authorization token and encrypted secret key.

        Returns
        -------
        string
              Admin authorization token.

        string
              Encrypted secret key to be stored in database.

        """

        # generate authentication token
        auth_token = secrets.token_urlsafe(16)

        # generate admin secret key
        admin_secret_key = secrets.token_hex(256)

        # generate a random salt
        salt = get_random_bytes(AES.block_size)

        # use the Scrypt KDF to get a private key from the password
        private_key = hashlib.scrypt(
            self.encrptyion_secret_key.encode(),
            salt=salt,
            n=2 ** 14,
            r=8,
            p=1,
            dklen=32,
        )

        # create cipher config
        cipher_config = AES.new(private_key, AES.MODE_GCM)

        # return a dictionary with the encrypted text
        cipher_text, tag = cipher_config.encrypt_and_digest(
            bytes(admin_secret_key, "utf-8")
        )
        encryption_dict = {
            "cipher_text": b64encode(cipher_text).decode("utf-8"),
            "salt": b64encode(salt).decode("utf-8"),
            "nonce": b64encode(cipher_config.nonce).decode("utf-8"),
            "tag": b64encode(tag).decode("utf-8"),
        }

        return (
            auth_token,
            urlsafe_b64encode(json.dumps(encryption_dict).encode()).decode(),
        )

    def decrypt(self, encrypted_secret_key):
        """
        Generates OneBridge Admin Authorization token and encrypted secret key.

        Parameters
        ----------Î
        encrypted_secret_key
            Encrypted secret key retireived from database.

        Returns
        -------
        string
              Admin secret key.
        """
        enc_dict = json.loads(urlsafe_b64decode(encrypted_secret_key.encode()).decode())

        # decode the dictionary entries from base64
        b64decode
        salt = b64decode(enc_dict["salt"])
        cipher_text = b64decode(enc_dict["cipher_text"])
        nonce = b64decode(enc_dict["nonce"])
        tag = b64decode(enc_dict["tag"])

        # generate the private key from the password and salt
        private_key = hashlib.scrypt(
            self.encrptyion_secret_key.encode(),
            salt=salt,
            n=2 ** 14,
            r=8,
            p=1,
            dklen=32,
        )

        # create the cipher config
        cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

        # decrypt the cipher text
        admin_secret_key = cipher.decrypt_and_verify(cipher_text, tag)

        return bytes.decode(admin_secret_key)
