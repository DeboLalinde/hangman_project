import random
from pathlib import Path


def get_random_word():
    wordlist_path = Path(__file__).with_name("wordlist.txt")

    with open(wordlist_path, "r", encoding="utf-8") as file:
        words = [line.strip().lower() for line in file if line.strip()]

    if not words:
        raise ValueError("La lista de palabras está vacía.")

    return random.choice(words)
    
