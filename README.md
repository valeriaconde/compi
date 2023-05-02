# Little Duck compiler

Este programa sirve para compilar y ejecutar el lenguaje LittleDuck. La gramática aceptada se encuentra en el archivo LittleDuck.g4 y utiliza la herramienta ANTLR para generar el lexer y el parser del lenguaje.

En el archivo main.py se encuentran el cubo semántico, las pilas de operadores, operandos, tipos y saltos, los diccionarios de memoria, y la virtual machine y el listener que encuentra los puntos neurálgicos y realiza las operaciones necesarias para evaluar las operaciones del programa.

En el archivo `main.py` usamos las listas `pilaTipos`, `pilaOperadores`, `pilaOperandos` y `pilaSaltos` donde guardamos la informacion que les corresponde a cada una conforme vamos leyendo el programa de prueba. Tenemos `var_table` que es un diccionario que representa la tabla de variables del programa. Este diccionario tiene el nombre de la variable como key y una dupla como valor, que se compone de tipo y direccion de memoria. `cuadruplos` es una lista de tuplas de cuatro valores, que en orden son el operador, var1, var2 y la variable donde se guardara el resultado. Luego tenemos una serie de constantes, `dirInts`, `dirFloat`, `dirCte_int`, `dirCte_float`, `dirBool` y `dirCte_str` que usamos para simular la direccion de memoria donde se van a guardar los datos. Y tenemos `constantes` que es un diccionario donde la llave es el valor real de la variable y el valor es la direccion de memoria donde se encuentra, y `memoria` que es un diccionario donde la llave es la direccion de memoria y el valor es el valor que contiene esa direccion de memoria. 

El cubo semantico es un arreglo de tres dimensiones donde cada nivel representa un operando, un operador y otro operando, y contiene el tipo de dato que resultara luego de realizarse dicha operacion.

En la funcion `vm()` que representa la virtual machine iteramos los cuadruplos que fueron generados durante la compilacion y realizamos las operaciones correspondientes, primero haciendo un mapeo en `memoria` para despues poder sacar los valores en tiempo constante de la direccion de memoria.

Es necesario contar con python3, antlr y java para correr el compilador.

En una línea de comando generamos los archivos necesarios a partir de la gramática con 

``` antlr4 -Dlanguage=Python3 LittleDuck.g4 ``` 

y después podemos correr el programa con nuestro propio input con 

``` python main.py testerprogram.txt ``` 

donde testerprogram.txt es el programa en lenguaje LittleDuck a compilar.
