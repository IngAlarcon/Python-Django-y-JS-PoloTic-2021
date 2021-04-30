'''
4.Escribe un programa en Python que muestre la hora actual con una suma de dos horas adicionales
'''
import datetime

horaActual = datetime.datetime.now()

hora = horaActual.hour
minutos = horaActual.minute

print(f"Hora actual {hora}:{minutos}")

hora += 2
#control de la hora si sobrepasa las 24hs

if hora > 24:
    hora -= 24

print(f"Dentro de 2 horas seran las {hora}:{minutos}")
