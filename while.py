i = 0
vezes = 0
soma = 0
numero = int(input("digite um numero: "))
while numero >= 0:
    i += 1
    vezes += 1
    soma += numero
    numero = int(input("digite um numero: "))
media = soma / vezes
print(f"media: {media}")