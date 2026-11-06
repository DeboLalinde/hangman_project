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

    def process_guess(self, letter):
        """Procesa una letra y devuelve True si está en la palabra."""
        self.guessed_letters.append(letter)
        if letter in self.word:
            return True
        else:
            self.errors = self.errors + 1
            return False

    def is_lost(self):
        """Devuelve True si se alcanzó el máximo de errores."""
        return self.errors >= self.max_errors

    def is_won(self):
        """Devuelve True si se adivinaron todas las letras."""
        return "_" not in self.display_progress()

    def display_progress(self):
        """Devuelve la palabra con las letras adivinadas y guiones."""
        progreso = ""
        for letra in self.word:
            if not letra.isalpha() or letra in self.guessed_letters:
                progreso = progreso + letra + " "
            else:
                progreso = progreso + "_ "
        return progreso.strip()
