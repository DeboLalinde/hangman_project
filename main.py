#!/usr/bin/env python3
"""Modulo main de Hangman game."""


def get_valid_letter(guessed_letters):
    """Pide al usuario que ingrese una letra."""
    while True:
        letter = input("Ingresa una letra: ").strip().lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Entrada invalida. Ingresa solo una letra.")
        elif letter in guessed_letters:
            print("Ya utilizaste esa letra. Proba con otra.")
        else:
            return letter
