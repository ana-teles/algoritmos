numeros = input().split()

numeros[0] = int(numeros[0])
numeros[1] = int(numeros[1])
numeros[2] = int(numeros[2])

original = numeros[:]

numeros.sort()

for numero in numeros:
    print(numero)

print("")

for numero in original:
    print(numero)

