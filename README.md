# Little Duck compiler

Este programa sirve para compilar y ejecutar el lenguaje LittleDuck. La gramática aceptada se encuentra en el archivo LittleDuck.g4 y utiliza la herramienta ANTLR para generar el lexer y el parser del lenguaje.

En el archivo main.py se encuentran el cubo semántico, las pilas de operadores, operandos, tipos y saltos, los diccionarios de memoria, y la virutal machine y el listener que encuentra los puntos neurálgicos y realiza las operaciones necesarias para evaluar las operaciones del programa.

Es necesario contar con python3, antlr y java para correr el compilador.

En una línea de comando generamos los archivos necesarios a partir de la gramática con `antlr4 -Dlanguage=Python3 LittleDuck.g4` y después podemos correr el programa con nuestro propio input con `python main.py testerprogram.txt` donde testerprogram.txt es el programa en lenguaje LittleDuck a copmilar.
