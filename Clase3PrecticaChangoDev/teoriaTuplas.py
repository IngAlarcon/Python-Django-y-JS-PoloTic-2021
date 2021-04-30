# Tuplas son otro tipo de coleccion son parecidas a las listas,
# son listas inmutables es decir a que no se pueden modificar
# agregar o editar una ves declaradas.

tupla = (4,"Hola",6.25,[5,9,7],6,4,8,"g")

#tupla.append(2) # Agregar un elemento no se puede
#tupla[2] = 8    # Editar un elemento nos e puede
#tupla.pop()     # No puedo eliminar


##### Lo que puedo hacer en las tuplas es buscar dentro de ellas y mostrar sus valores o un rango de valor ############

print(tupla)

print(tupla[1])
print(tupla[-2])
print(tupla[2:4])

#Buscando dentro de la tupla

print(f"Busco el N° 4 en mi tupla: {4 in tupla}")
print(f"Busco el indice del dato hola en mi tupla: {tupla.index('Hola')}")
print(f"Busco cauntas veces esta el N° 4 en mi tupla:{tupla.count(4)}")


### Tranformar tuplas en lista y viceversa ###

tuplaAlista = list(tupla)
print(f"Tranforme mi tupla a lista: {tuplaAlista}")

# Tranformar de lista a tupla
lista = [5, 8, 5.3, "jk","poo"]

listaAtupla = tuple(lista)

print(f"Mi lista: {lista}")
print(f"Transformo mi lista  a tupla: {listaAtupla}")
