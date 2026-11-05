class HangmanGame:
    """Representa una partida del juego del ahorcado."""

    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0
