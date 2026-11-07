#!/usr/bin/env python3
"""Modulo main de Hangman game."""
from game import HangmanGame
from utils import get_random_word


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
    print(game.display_progress())

    remaining_attempts = game.max_errors - game.errors

    print("\nIntentos restantes:", remaining_attempts, "de", game.max_errors)

    print("\nLetras utilizadas:", ",".join(game.guessed_letters))

    print("-------------------------------------------\n")


def play_game():
    """Ejecuta una partida del ahorcado."""

    word = get_random_word()
    game = HangmanGame(word)

    display_game_status(game)

    while not game.is_won() and not game.is_lost():
        letter = get_valid_letter(game.guessed_letters)
        game.process_guess(letter)
        display_game_status(game)

    if game.is_won():
        print("¡Ganaste!")
    else:
        print("Fin del juego")
        print("La palabra era:", game.word)


def main():
    """Inicia el juego y permite jugar nuevamente."""

    while True:
        play_game()

        answer = input("\nQueres jugar otra partida? (si/no): ").strip().lower()

        if answer != "si":
            print("Gracias por jugar!")
            break

if __name__ == "__main__":
    main()
