i = 0
soma = 0
recebe = ([0,1,2,3])
for i in range(4):
    recebe[i] = int(input(f"nota {i + 1}: "))
    while recebe[i] < 0 or recebe[i] > 10:
        recebe[i] = int(input(f"nota {i + 1}: "))
    soma = soma + recebe[i]
    i += 1
media = soma / 4
print(f"media: {media}")
if media >= 7:
    print("aprovado")
elif media >= 5:
    print("recuperação")
elif media < 5:
    print("reprovado")