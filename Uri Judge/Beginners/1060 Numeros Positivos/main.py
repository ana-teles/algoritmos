quantidade = 0

for i in range(6):
    numero = float(input())
    if numero > 0:
        quantidade += 1
        
print(f"{quantidade} valores positivos")
