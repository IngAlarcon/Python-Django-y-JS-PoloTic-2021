# Diccionarios son otro tipo de coleccion donde los elementos se guardan desordenados
# La caracteristica principal es que tienen dos elementos por pocicion clave y valor; no puede haber claves duplicadas

diccionario = {}  #Es un diccionario vacio

print(diccionario)


diccionario = {"azul":"blue", "rojo":"red", "verde":"green"}

print(diccionario)

print(diccionario["rojo"])

#gregar elemento al diccionario se agregan de forma desordenada

diccionario["amarillo"] = "yellow"

print(diccionario)

#Modificar elemento al diccionario

diccionario["azul"] = "bluerider"

print(diccionario)

#Eliminar elemento del diccionario

del(diccionario["rojo"]) #Al eliminar una clave tambien se elimina el valor

print(diccionario)

#Los diccionarios aceptan otros tipos de datos y otras colecciones, listas tuplas y otros diccionarios
#Agenda sencilla

agenda = {"Walter":[22, 1.73],"Leandro":[19, 1.75],"Mariano":{"edad":29, "estatura":1.69}}
print(agenda)
print(agenda["Walter"])
print(agenda["Mariano"])


####################Diccionarios############

equipo = {10:"Paulo Dybala",11:"Douglas Costa",7:"Cristiano Ronaldo",17:"Mario Manzukic" }

print(equipo)
print(equipo[7])

# Si no hay un valor en mi Diccionario puedo resolverlo con un mensaje

print(equipo.get(7,"No existe un jugador con esa camiseta"))
print(equipo.get(12,"No existe un jugador con esa camiseta"))

#Busqueda en nuetro diccionario

print( 10 in equipo)
print( 12 in equipo)

#Mostrar todas las claves de mi diccionario

print(equipo.keys()) #Mostrando solo las claves de mi diccionario
print(equipo.values()) #Mostrando solo los valores de mi diccionario

#Mostrar clave y valor de mi diccionario en formato de tuplas

print(equipo.items())

#Contando elementos
print(len(diccionario))

#Eliminando
equipo.clear()
print(equipo)

