# Welcome to Secure Code Game Season-1/Level-5!

# This is the last level of our first season, good luck!

import binascii
import random
import secrets
import hashlib
import os
import bcrypt

from argon2 import PasswordHasher

class Random_generator:

    # generates a random token
    def generate_token(self, length=8, alphabet=(
    '0123456789'
    'abcdefghijklmnopqrstuvwxyz'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    )):
        return ''.join(random.choice(alphabet) for _ in range(length))

    # generates salt
    def generate_salt(self, rounds=12):
        salt = ''.join(str(random.randint(0, 9)) for _ in range(21)) + '.'
        return f'$2b${rounds}${salt}'.encode()

class SHA256_hasher:

    # produces the password hash by combining password + salt because hashing
    def password_hash(self, password, salt):
        ph = PasswordHasher()
        return ph.hash(password)

    # verifies that the hashed password reverses to the plain text version on verification
    def password_verification(self, password, password_hash):
        ph = PasswordHasher()
        return ph.verify(password_hash, password)

class MD5_hasher:

    # same as above but using a different algorithm to hash which is MD5
    def password_hash(self, password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt(5)).decode()

    def password_verification(self, password, password_hash):
        return bcrypt.checkpw(password.encode(), password_hash.encode())

# a collection of sensitive secrets necessary for the software to operate
PRIVATE_KEY = os.environ.get('PRIVATE_KEY')
PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
SECRET_KEY = 'TjWnZr4u7x!A%D*G-KaPdSgVkXp2s5v8'
PASSWORD_HASHER = 'MD5_hasher'

# Contribute new levels to the game in 3 simple steps!
# Read our Contribution Guideline at github.com/skills/secure-code-game/blob/main/CONTRIBUTING.md