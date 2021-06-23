inicio, fim = [int(x) for x in input().split()]  

duracao = fim - inicio

if duracao <= 0:
    duracao += 24

print(f"O JOGO DUROU {duracao} HORA(S)")