'''
2. Escribe un programa Python que acepte un número entero (n) y calcule
el valor de n + nn + nnn
'''

n = int(input("Digite un numero entero: "))

calculo = n + n*n + n*n*n

print(f"El valor de {n} + {n}*{n} + {n}*{n}*{n} es: {calculo}")