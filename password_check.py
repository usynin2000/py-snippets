import base64
import hashlib
import hmac
import logging

from passlib.context import CryptContext

import os
from dotenv import load_dotenv

load_dotenv()


SALT = os.getenv('SALT')


logger = logging.getLogger(__name__)

pwd_context = CryptContext(schemes=["md5_crypt"], deprecated="auto")


def encode_string(value: str) -> bytes:
    """Encodes a string to bytes using UTF-8."""
    return value.encode("utf-8")


def get_hmac(password: str) -> str:
    """Returns a Base64 encoded HMAC+SHA512 hash of the password signed with the salt."""

    salt = SALT

    if salt is None:
        raise RuntimeError(
            "The configuration value `SECURITY_PASSWORD_SALT` must not be None."
        )

    # временное решение c hashlib.md5() и игнорирование безопасности, на этапе переезда с flask-security
    p_hash = hashlib.md5()  # nosec B324
    p_hash.update(encode_string(password))
    password_bytes = p_hash.digest()

    h = hmac.new(
        encode_string(salt),
        password_bytes,
        hashlib.sha512,
    )
    return base64.b64encode(h.digest()).decode("ascii")


def encrypt_password(password: str) -> str:
    """Encrypts the password using both HMAC and passlib."""
    signed_password = get_hmac(password)
    return pwd_context.hash(signed_password)


def verify_password(
    password: str,
    account_password: str = "$1$f.blB2UV$3m7tQL51zjMCWOPdFXE7z/"
) -> bool:
    """Verifies the password and updates the stored hash if needed."""
    try:
        stored_password = account_password

        if pwd_context.identify(stored_password) != "plaintext":
            password = get_hmac(password)

        return pwd_context.verify(password, stored_password)

    except Exception as exc:
        logger.warning("Password verification failed. Error: %s", str(exc))
        return False

if __name__ == "__main__":
    stored_hash = encrypt_password("secret123")
    print(stored_hash)

