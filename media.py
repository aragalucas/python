i = 0
recebe = ([0,1,2,3])
soma = 0
for i in range(4):
    recebe[i] = int(input(f"nota {i + 1}: "))
    soma = soma + recebe[i]
    i += 1
media = soma / 4
print(f"media: {media}")