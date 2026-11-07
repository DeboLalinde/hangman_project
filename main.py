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


def display_game_status(game):
    """Muestra el progreso actual de la partida."""
    print("\n---=== HANGMAN ===---")

    print("\nPalabra:")
    game.display_progress()

    remaining_attempts = game.max_errors - game.errors

    print("\nIntentos restantes:", remaining_attempts, "de", game.max_errors)

    print("\nLetras utilizadas:", ",".join(game.guessed_letters))


    print("-------------------------------------------\n")
