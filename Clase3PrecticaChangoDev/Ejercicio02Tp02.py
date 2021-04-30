'''

Escribe un programa Python que acepte 5 números decimales del usuario.

'''
"""
#Posible solucion 1
numFloat = []
while True:
    numeroIngresado = input("Ingrese numeros al programa: ")

    if numeroIngresado.isdigit() != True: #El isdigit() método devuelve True si todos los caracteres son dígitos; de lo contrario, False.
        numFloat.append(numeroIngresado)
    cantidadNum = len(numFloat)

    if cantidadNum == 5:
        break

for i in range(cantidadNum):

    print(numFloat[i]) 
    
"""
#Posible solucion 2 la mas aceptable desde mi punto de vista

numFloat = []

while True:
    numeroIngresado = input("Ingrese numeros al programa: ")
    comprobando = numeroIngresado.find(".")# El find() método encuentra la primera aparición del valor especificado.
    print(comprobando)                     # El find() método devuelve -1 si no se encuentra el valor.

    if comprobando != -1:
        try:
            valorFloat = float(numeroIngresado)
            numFloat.append(valorFloat)
        except:
            print("No es un Numoro")

    cantidadNum = len(numFloat)
    if cantidadNum == 5:
        break

for i in range(cantidadNum):

    print(f" {i+1}° numeros decimales aceptados por el programa: {numFloat[i]}")
