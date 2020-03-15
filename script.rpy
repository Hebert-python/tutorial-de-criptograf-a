# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define p = Character("Profesor")

image michi = "michi.png"

# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

scene aula

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

show profesor

    # Presenta las líneas del diálogo.

"Bienbenido al tutorial de criptografía"

"¿Sobre que tema desea aprender?"

show profesor at left

label inicio:
menu:
    "¿Qué es la criptografía?":
        "Disciplina que estudia el arte de la escritura en clave, bajo códigos alfabéticos, cuyo principio radica en la valoración que se dé a cada letra, reemplazándola."
        jump inicio
    "Criptograma":
        "Es un texto cifrado, y el convertirlo de nuevo al lenguaje claro se llama descifrarlo."
        jump inicio
    "Alfabetos Decalados":
        show decalado at topright
        "El alfabeto decalado es aquel en el cual cada letra se reemplaza por la que está tantos lugares antes o tantos después dentro de una serie, según como se haya convenido."
        hide decalado
        jump inicio
    "Clave Michi":
        show michi at topright
        "A base de puntos y rayas que disponen cuadrantes. Los podemos emplear de dos modos."
        hide michi
        jump inicio
    "Frecuencias en los textos":
        show frecuencia at topright
        "Aunque se utilicen alfabetos de lo más desordenados, un experto puede descifrar con relativa facilidad un texto escrito en clave, pues cada letra se presenta en cada idioma con una frecuencia relativa propia, como puede verse en el cuadro."
        "Lógicamente, los descifradores deben saber primero en qué idioma ha sido redactado el mensaje."
        hide frecuencia
        jump inicio
# Finaliza el juego:

return
