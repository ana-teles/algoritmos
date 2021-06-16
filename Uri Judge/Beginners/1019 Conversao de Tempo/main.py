tempo = int(input())

horas = tempo // 3600

tempo %= 3600
minutos = tempo // 60

tempo %= 60

print(f"{horas}:{minutos}:{tempo}")