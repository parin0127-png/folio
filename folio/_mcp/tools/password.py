import string
import secrets

def password_generator(length: int = 16):
    """generate a strong, secure, and random password of any specified length"""
    try:
        chars = string.ascii_letters + string.digits + string.punctuation + string.hexdigits
        password = "".join(secrets.choice(chars) for _ in range(length))
        return {"password" : password, "length": length}
    except Exception as e:
        return f"> Password generator failed: {str(e)}"
