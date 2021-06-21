codigo, quantidade = input().split()
codigo, quantidade = int(codigo), int(quantidade)

precos = [0.0, 4.00, 4.50, 5.0, 2.0, 1.5]

total = precos[codigo] * quantidade

print(f'Total: R$ {total:.2f}')

