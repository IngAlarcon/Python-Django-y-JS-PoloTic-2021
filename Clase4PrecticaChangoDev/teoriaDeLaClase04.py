"""
Tratamiento de Excepciones
    try ...
    except ...
"""
import sys

try:
    numero1 = int(input("Ingrese primer numero: "))
    numero2 = int(input("Ingrese segundo numero: "))

except ValueError:
    print("Error: Valor no valido.")
    #Salir del programa
    sys.exit(1)

try:
    resultado = numero1 / numero2

except ZeroDivisionError:
    print("Error: No se puede dividir por 0.")

    #Salir del programa
    sys.exit(1)

print(f"{numero1} / {numero2} = {resultado}")

print("######  finally Ejemplo: Ejemplo intentando abrir y escribir a un archivo que es de solo lectura:##########################")


try:
    f = open("archivoejemplo.txt", "w")
    f.write("Linea de prueba dentro del archivo.")
    print("En el archivo .txt se escribio 'Linea de prueba dentro del archivo.'")
except:
    print("Algo ocurrio al intentar abrir el archivo.")

finally:
    print("El try y except finalizo")
    f.close()