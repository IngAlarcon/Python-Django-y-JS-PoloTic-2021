#Set o Conjuntos es un tipo de coleccion donde los elemntos se agregan de forma desordenada
# grupos de elementos desarodenados cuya caraqcteristica es que no puede haber duplicados

conjunto = set() # Cuando quiero declarar un conjunto vacio

conjunto = {1,2,3,"Hola",4.365,"G"}
print(conjunto)

# Dentro de mi conjunto no puede haber otras colecciones
# conjunto = {1,2,3,"Hola",4.365,[1,2,3],"G"} # esto no es valido

#En el conjunto se puede agregar valores duplicados pero este mismo solo los guarda una sola ves cada valor dentro del conjunto

#Agregando elemento a mi conjunto

conjunto.add(5) # se agrega de forma desordenada
conjunto.add("Que tal")
conjunto.add("P")
print(conjunto)
#Si queremos eliminar un elemento de mi coleccion

conjunto.discard(3)
print(f"Se elimino el 3 de mi coleccion: {conjunto}")

#Buscar en mi coleccion

print( 4.365 in conjunto)
print( 4.365 not in conjunto)

print( "F" in conjunto)
print( "F" not in conjunto)


#como limiar mi coleccion por completo
conjunto.clear()
print(conjunto)

#Lo que puedo hacer con los conjuntos
#Comparacion
a = { 1, 2, 3}
b = { 3, 4, 5}
print(f"Conjunto a: {a}")
print(f"Conjunto b: {b}")
#Comparando conjuntos

print(f"Comparando si son iguales: {a == b}")
######################################################
a = { 1, 2, 3}
b = { 3, 2, 1}
print(f"Conjunto a: {a}")
print(f"Conjunto b: {b}")
#Comparando conjuntos

print(f"Comparando si son iguales: {a == b}")
print(f"Tengo : {len(b)} elementos en mi conjunto")

# Operaciones entre conjuntos
# Union entre dos conjuntos
a = { 1, 2, 3}
b = { 3, 4, 5}

print(f"Conjunto a: {a}")
print(f"Conjunto b: {b}")

c = a | b  # | con este signo establesco la union de dos conjuntos

print(f"Union entre dos conjuntos a | b: c= {c}")

# Interseccion entre dos conjuntos
a = { 1, 2, 3}
b = { 3, 4, 5}

print(f"Conjunto a: {a}")
print(f"Conjunto b: {b}")

c = a & b  # & con este signo establesco la interseccion de dos conjuntos

print(f"Interseccion entre dos conjuntos a & b: c= {c}")

# Diferencia entre dos conjuntos
a = { 1, 2, 3}
b = { 3, 4, 5}

print(f"Conjunto a: {a}")
print(f"Conjunto b: {b}")

c = a - b  # elementos que no estan en el conjunto de  a y no en el de b

print(f"Diferencia entre dos conjuntos a - b: c= {c}")


# Diferencia simetrica entre dos conjuntos
a = { 1, 2, 3}
b = { 3, 4, 5}

print(f"Conjunto a: {a}")
print(f"Conjunto b: {b}")

c = a ^ b  # ^ son elementos que estan en a y en b es decir no me muetsra la interseccion

print(f"Diferencia simetrica  entre dos conjuntos a ^ b: c= {c}")