import secrets
from Crypto.Cipher import AES


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
        cipher = AES.new(str.encode(self.encrptyion_secret_key), AES.MODE_EAX)
        auth_token = secrets.token_urlsafe(16)
        admin_secret_key = secrets.token_hex(16)
        encrypted_secret_key, _ = cipher.encrypt_and_digest(
            str.encode(admin_secret_key, encoding="UTF-8")
        )
        return auth_token, encrypted_secret_key.decode(encoding="UTF-8")

    def decrypt(self, encrypted_secret_key):
        """
        Generates OneBridge Admin Authorization token and encrypted secret key.

        Parameters
        ----------
        encrypted_secret_key
            Encrypted secret key retireived from database.

        Returns
        -------
        string
              Admin secret key.
        """
        cipher = AES.new(str.encode(self.encrptyion_secret_key), AES.MODE_EAX)
        nonce = cipher.nonce
        cipher = AES.new(
            str.encode(self.encrptyion_secret_key), AES.MODE_EAX, nonce=nonce
        )
        admin_secret_key = cipher.decrypt(encrypted_secret_key)
        return admin_secret_key
