import string
import random

BASE62_ALPHABET = string.ascii_uppercase + string.ascii_lowercase + string.digits
BASE62_RADIX = len(BASE62_ALPHABET)

def generate_short_code(length=6):
    """Generate a random short code of the given length."""
    return ''.join(random.choice(BASE62_ALPHABET) for _ in range(length))

def encode_url(short_code=None):
    """
    Convert short code into short url.
    If a short code is provided, use it; otherwise, generate a new one.
    """
    if short_code is None:
        short_code = generate_short_code()
    return f"http://short.est/{short_code}"

def decode_url(short_url):
    """Decode the given short URL into the original long URL."""
    short_code = short_url.split('/')[-1]
    return short_code