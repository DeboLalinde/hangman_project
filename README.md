# hangman_project

## Descripción

El objetivo del juego es adivinar una palabra secreta, ingresando letras una por una. El jugador cuenta con un máximo de 6 errores antes de perder la partida.

Todas las palabras y frases están relacionadas con la tecnología y la informática, como "teclado", "base de datos" o "inteligencia artificial".

## Requisitos

- Python 3 instalado.

## Cómo ejecutar el juego

1. Descargar o clonar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

```bash
python3 main.py
```

## Archivos del proyecto

- `main.py`: inicia y controla el juego.
- `game.py`: contiene la lógica y las reglas del ahorcado (clase `HangmanGame`).
- `utils.py`: selecciona una palabra aleatoria.
- `wordlist.txt`: contiene la lista de palabras y frases disponibles.

## Reglas

- El jugador debe ingresar una letra por turno.
- Solo se aceptan letras como entrada válida.
- No se puede repetir una letra ya intentada.
- Cada letra incorrecta suma un error.
- Se permiten hasta 6 errores.
- Los espacios y signos (como guiones) se muestran automáticamente.
- El jugador gana si descubre todas las letras de la palabra antes de alcanzar el máximo de errores.

## Integrantes

- Romina Castro
- Deborah Lalinde
- Florencia Carrion