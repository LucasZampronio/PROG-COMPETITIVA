numero_segundos = int(input())

horas = numero_segundos // 3600
minutos = (numero_segundos % 3600) // 60
segundos = numero_segundos % 60

print(f"{horas}:{minutos}:{segundos}")


