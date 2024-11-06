import random
import string
import os
from config import images


def generate_random_string(length: int) -> str | None:
    letters_and_digits = string.ascii_letters + string.digits  # Буквы и цифры
    return "".join(random.choice(letters_and_digits) for i in range(length))


def remove_file(name: str):
    os.remove(f"{images}/{name}")
