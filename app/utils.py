import random
import string
import os
from config import images

def generate_random_string(length: int) -> str | None:
    letters_and_digits = string.ascii_letters + string.digits  # Буквы и цифры
    return "".join(random.choice(letters_and_digits) for i in range(length))

def get_file_by_id(id: str) -> str:
    """функция возвращает действующее имя файла"""
    files: list = os.listdir(images)
    for name in files:
        if name.startswith(id):
            return name
    else:
        return None

def remove_file(name: str):
    os.remove(f"{images}/{name}")