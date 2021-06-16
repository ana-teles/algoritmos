valor = int(input())

print(valor)

resultado = valor // 100
print(f"{resultado} nota(s) de R$ 100,00")
valor %= 100

resultado = valor // 50
print(f"{resultado} nota(s) de R$ 50,00")
valor %= 50

resultado = valor // 20
print(f"{resultado} nota(s) de R$ 20,00")
valor %= 20

resultado = valor // 10
print(f"{resultado} nota(s) de R$ 10,00")
valor %= 10

resultado = valor // 5
print(f"{resultado} nota(s) de R$ 5,00")
valor %= 5

resultado = valor // 2
print(f"{resultado} nota(s) de R$ 2,00")
valor %= 2

print(f"{valor} nota(s) de R$ 1,00")
