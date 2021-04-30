"""
3.
Escribe un programa en Python que reciba 5 números enteros del usuario y los guarde en una lista.
Luego recorrer la lista y mostrar los números por pantalla.

"""

listaEnteros = []

contador = 0

while contador < 5:
    numero = int(input("Escribe un número entero: "))
    listaEnteros.append(numero) # Guardando los numeros enteros en mi lista
    contador = contador + 1

# Recorre la lista e imprime los números de la lista
for i in range(len(listaEnteros)):
  print(f"{i+1}° entero de mi lista: {numero}")
