numeros = input().split()

numeros[0] = float(numeros[0])
numeros[1] = float(numeros[1])
numeros[2] = float(numeros[2])

if max(numeros) >= (sum(numeros) / 2):
    area = (numeros[0] + numeros[1]) * (numeros[2] / 2)
    print(f"Area = {area:.1f}")

else:
    perimetro = sum(numeros)
    print(f"Perimetro = {perimetro:.1f}")

