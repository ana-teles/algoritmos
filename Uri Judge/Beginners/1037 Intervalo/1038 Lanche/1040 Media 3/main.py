n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")

elif media < 5.0:
    print("Aluno reprovado.")

else: 
    print("Aluno em exame.")
    exame = float(input())
    print(f"Nota do exame: {exame:.1f}")  
    media = (exame + media) / 2
    if media >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media:.1f}")


