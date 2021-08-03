one-bridge-admin-cipher
=========

[![CI-CD](https://github.com/Fritek/one-bridge-admin-cipher/actions/workflows/ci.yaml/badge.svg)](https://github.com/Fritek/one-bridge-admin-cipher/actions/workflows/ci.yaml)
[![pre-commit](https://github.com/Fritek/one-bridge-admin-cipher/actions/workflows/pre-commit.yaml/badge.svg)](https://github.com/Fritek/one-bridge-admin-cipher/actions/workflows/pre-commit.yaml)


An internal One Bridge Python library to handle admin related crpytographic functionalities.


Installing
----------

Run the following comand to install the library in your pythion virtual environment

pip install git+https://github.com/Fritek/one-bridge-admin-cipher.git#egg=one-bridge-admin-cipher


Example
----------

This code snippets desribes how the package can be used depending on your use case

import secrets

from one_bridge_admin_cipher.one_bridge_admin_cipher import OBACipher

## Generate Secret Key
test_secret_key = secrets.token_hex(256)

# Instantiate module class with secret key
cipher = OBACipher(encrptyion_secret_key=test_secret_key);

# Generate auth token and encrypted_secret_key
auth_token, encrypted_secret_key = cipher.generate_keys()

# Recover admin_secret_key
admin_secret_key = cipher.decrypt(encrypted_secret_key=encrypted_secret_key)



Developing
----------

This project uses ``black`` to format code and ``flake8`` for linting. We also support ``pre-commit`` to ensure
these have been run. To configure your local environment please install these development dependencies and set up
the commit hooks.

.. code-block:: bash

   $ pip install black flake8 pre-commit
   $ pre-commit install

Testing
-------

This project uses ``pytest`` to run tests and also to test docstring examples.

Install the test dependencies.

.. code-block:: bash

   $ pip install -r requirements_test.txt

Run the tests.

.. code-block:: bash

    $ pytest
    === 3 passed in 0.13 seconds ===
