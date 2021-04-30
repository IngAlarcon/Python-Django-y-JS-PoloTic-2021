"""
4.
Dada una lista (lista1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200 ]), iterarla y
mostrar números divisibles por cinco, y si encuentra un número mayor que 150, detenga la iteración
del bucle.

"""

lista1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

print(f"Mi lista: {lista1}")

listaDivisible = []

for i in range(len(lista1)):
    if lista1[i] % 5 == 0 and lista1[i] < 150:
         listaDivisible.append(lista1[i])

print(f"Los Numeros de la lista que son divisibles por 5 y hasta 150 son: {listaDivisible}")
