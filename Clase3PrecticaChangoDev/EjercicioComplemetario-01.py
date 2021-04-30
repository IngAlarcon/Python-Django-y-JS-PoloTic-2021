'''

Ejercicio 1:

  Escriba un programa donde tenga un lista y que, a continuacion,
 elimine los elemnetos repetidos, por ultimo mostrar la lista

'''

miLista = [5,9,6,3,8,56,47,3,84,9,3]

print(f"Mi lista: {miLista}")

#Solucion lo que podemos hacer es convertir mi lista a un conjunto ya que este no permite valores repetidos
# pero como no podemos dejarlo como un conjunto lo volvemos a tranformar en una lista

#Se pudo resolver en una sola linea
#miLista = list(set(miLista))


pasandoAConjunto = set(miLista)
print(f"Mi lista tranformada en conjunto donde se elimino los valores repetido: {pasandoAConjunto}")

miLista = list(pasandoAConjunto)
print(f"Mi lista sin valores repetido: {miLista}")




