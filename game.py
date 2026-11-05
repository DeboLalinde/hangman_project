class HangmanGame:
    """Representa una partida del juego del ahorcado."""

    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        """Devuelve la palabra con las letras adivinadas y guiones."""
        progreso = ""
        for letra in self.word:
            if letra in self.guessed_letters:
                progreso = progreso + letra + " "
            else:
                progreso = progreso + "_ "
        return progreso.strip()
