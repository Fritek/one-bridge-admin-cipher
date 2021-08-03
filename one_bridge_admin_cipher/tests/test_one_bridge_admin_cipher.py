import pytest
import secrets


from one_bridge_admin_cipher import OBACipher

test_secret_key = secrets.token_hex(16)


def test_initialization():
    test_obj = OBACipher(encrptyion_secret_key=test_secret_key)
    assert test_obj.encrptyion_secret_key != None


def test_generate_keys():
    test_obj = OBACipher(encrptyion_secret_key=test_secret_key)
    admin_auth, encrypted_secret_key = test_obj.generate_keys()
    assert admin_auth != None
    assert encrypted_secret_key != None


def test_decrypt():
    test_obj = OBACipher(encrptyion_secret_key=test_secret_key)
    admin_auth, encrypted_secret_key = test_obj.generate_keys()
    admin_secret_key = test_obj.decrypt(encrypted_secret_key)
    assert admin_secret_key != None
