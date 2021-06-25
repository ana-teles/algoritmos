salario = float(input())


if salario >= 0 and salario <= 400.00:   
    reajuste = 0.15 * salario
    salario += reajuste
    print(f"Novo salario: {salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print("Em percentual: 15 %")

elif salario >= 400.01 and salario <= 800.00:   
    reajuste = 0.12 * salario
    salario += reajuste
    print(f"Novo salario: {salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print("Em percentual: 12 %")

elif salario >= 800.01 and salario <= 1200.00:   
    reajuste = 0.10 * salario
    salario += reajuste
    print(f"Novo salario: {salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print("Em percentual: 10 %")

elif salario >= 1200.01 and salario <= 2000.00:   
    reajuste = 0.07 * salario
    salario += reajuste
    print(f"Novo salario: {salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print("Em percentual: 7 %")

elif salario >= 2000.01:
    reajuste = 0.04 * salario
    salario += reajuste
    print(f"Novo salario: {salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print("Em percentual: 4 %")