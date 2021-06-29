salario = float(input())

taxa = 0 

if salario > 4500.00:
    taxa += (salario - 4500.00) * 0.28
    salario = 4500.00

if salario >= 3000.01:
    taxa += (salario - 3000.00) * 0.18
    salario = 3000.00

if salario >= 2000.01:
    taxa += (salario - 2000.00) * 0.08
    print(f"R$ {taxa:.2f}")

else:
    print("Isento")