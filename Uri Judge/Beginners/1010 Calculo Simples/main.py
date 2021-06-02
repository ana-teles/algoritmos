peca1 = input().split()
quant1 = int(peca1[1])
valor1 = float(peca1[2])


peca2 = input().split()
quant2 = int(peca2[1])
valor2 = float(peca2[2])

total = quant1 * valor1
total += quant2 * valor2

print(f"VALOR A PAGAR: R$ {total:.2f}")

