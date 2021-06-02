nome = input()

salario = float(input())
vendas = float(input())
comissao = 0.15

print(f"TOTAL = R$ {vendas * comissao + salario:.2f}")