numero1, operador, numero2 = input().split()

numero1 = float(numero1)
numero2 = float(numero2)

if operador == "+":
    print(numero1 + numero2)

elif operador == "-":
    print(numero1 - numero2)

elif operador == "*":
    print(numero1 * numero2)

elif operador == "/":
    print(numero1 / numero2)

