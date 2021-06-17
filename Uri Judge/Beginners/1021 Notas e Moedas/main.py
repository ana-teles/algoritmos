valor = round(float(input()) * 100)

print("NOTAS:")

resultado = valor // (100 * 100)
print(f"{resultado} nota(s) de R$ 100.00")
valor %= 10000

resultado = valor // 5000
print(f"{resultado} nota(s) de R$ 50.00")
valor %= 5000

resultado = valor // 2000
print(f"{resultado} nota(s) de R$ 20.00")
valor %= 2000

resultado = valor // 1000
print(f"{resultado} nota(s) de R$ 10.00")
valor %= 1000

resultado = valor // 500
print(f"{resultado} nota(s) de R$ 5.00")
valor %= 500

resultado = valor // 200
print(f"{resultado} nota(s) de R$ 2.00")
valor %= 2000

print("MOEDAS:")

resultado = valor // 100
print(f"{resultado} moeda(s) de R$ 1.00")
valor %= 100

resultado = valor // 50
print(f"{resultado} moeda(s) de R$ 0.50")
valor %= 50

resultado = valor // 25
print(f"{resultado} moeda(s) de R$ 0.25")
valor %= 25

resultado = valor // 10
print(f"{resultado} moeda(s) de R$ 0.10")
valor %= 10

resultado = valor // 5
print(f"{resultado} moeda(s) de R$ 0.05")
valor %= 5

resultado = valor
print(f"{resultado} moeda(s) de R$ 0.01")

