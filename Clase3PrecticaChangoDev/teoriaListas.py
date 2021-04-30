# Una Listases una estructura de datos muy flexsible, se le puede agregar diferente tipos de datos

lista = ["Lunes","Martes","Miercoles","Juevas","Viernes",40,5.67,[1,2,3],True]

print(f"Mi lista: {lista} ")

# Para saber la cantidad de elementos que tengo en mi lista uso la funcion len()

print("##### Cantidad de elementos en mi lista usando lent() ######")

print(f"Cantidad de elementos: {len(lista)}")


# Agregar elementos a mi lista  con .append(valor) me agreaga al final de la lista
listaAgregar = [1,2,3,4]

listaAgregar.append(5)
listaAgregar.append("Chango")

print(listaAgregar)

# Agregar elementos a mi lista  con .insert() se pasan dos parametros el indice donde quiero que se agregue y segundo el valor

listaAgregar.insert(0, 0)
listaAgregar.insert(6, "Development")

print(listaAgregar)

# Agregar varios elementos a mi lista con .extend() es decir puede concatener una lista en una lista que  me agreaga al final de la lista original

listaAgregar.extend([6,7,8])

print(listaAgregar)

# Si quiero buscar un determinado elemento en mi lista uso "in" para armar una condicion ej: (valorAencontrar in miLista)
# si lo encuentra en la lista me retorna True y si no esta me retorna False

print(f"Esta en la lista: {4 in listaAgregar}")
print(f"Esta en la lista: {'Chango' in listaAgregar}")
print(f"No esta en la lista: {'Walter' in listaAgregar}")

#Si quiero saber en que posicion de mi lista esta el valor uso .index() tengo que pasar el valor y me retorna el indice

print(f"El elemento esta en el indice: {listaAgregar.index('Chango')}")

# Si quiero buscar valores repetido en mi lista uso la funcion .count() pasando el valor que quiero buscar

listaAgregar.extend([2,4,8,"alarcon",0,"a",4])

print(listaAgregar)

print(f"Cuantos valores 4 ahy en mi lista: {listaAgregar.count(4)}")


# Para eliminar podemos usar la funcion .pop() si no pasamos ningun valor me elimina el ultimo elemento de mi lista
# si queremos eliminar un valor espesifico pasamos el indice de dicho valor

listaAgregar.pop(7)
print(f"Se paso el indice 7, Chango se elimino de mi lista: {listaAgregar}")

#Eliminar un dato de  mi lista con pasar el dato que quiero eliminar

listaAgregar.remove('alarcon')

print(f"Elimino alarcon de mi lista con remove: {listaAgregar}")

# Borrar todos los datos de mi lista con .clear()

listaAgregar.clear()

print(f"Elimino toda mi lista con clear: {listaAgregar}")

# Ordenar mi lista
listaAordenar = [6,-2,6,9,7,0,3]

listaAordenar.sort()

print(listaAordenar)
