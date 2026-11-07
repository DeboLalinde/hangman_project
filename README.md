hangman_project

Juego del ahorcado en consola desarrollado en Python, en equipo, como parte de la Certificación Construyendo con IA.

Descripción

El objetivo del juego es adivinar una palabra secreta, ingresando letras una por una. El jugador cuenta con un máximo de 6 errores antes de perder la partida.

Requisitos

•⁠  ⁠Python 3 instalado.

Cómo ejecutar el juego

1.⁠ ⁠Descargar o clonar el repositorio.
2.⁠ ⁠Abrir una terminal en la carpeta del proyecto.
3.⁠ ⁠Ejecutar:

python3 main.py

Archivos del proyecto

•⁠  ⁠main.py: inicia y controla el juego.
•⁠  ⁠game.py: contiene la lógica y las reglas del ahorcado.
•⁠  ⁠utils.py: selecciona una palabra aleatoria.
•⁠  ⁠wordlist.txt: contiene la lista de palabras disponibles.

Reglas

•⁠  ⁠El jugador debe ingresar una letra por turno.
•⁠  ⁠Cada letra incorrecta suma un error.
•⁠  ⁠Se permiten hasta 6 errores.
•⁠  ⁠El jugador gana si descubre todas las letras de la palabra antes de alcanzar el máximo de errores.
