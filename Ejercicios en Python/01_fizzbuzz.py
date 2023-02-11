###   Retos de Programación   ###

"""
RETO #1
EL FAMOSO "FIZZ BUZZ":
Escribe un programa que muestre por consola (con un print) los
numeros del 1 al 100 (ambos incluidos y con salto de linea entre 
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
Multiplos de 3 y 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    for index in range(1, 101):
        if index %3 == 0 and index %5 == 0:
            print ("fizzbuzz")
        elif index %3 == 0:
            print ("fizz")
        elif index %5 == 0:
            print ("buzz")
        else:
            print(index)

fizzbuzz()

### CORRIENDO CON EXITO ###