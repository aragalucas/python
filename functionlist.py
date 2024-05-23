numeros = []
def pares(numeros):
    pares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
    return pares
def impares(numeros):
    impares = 0
    for numero in numeros:
        if numero % 2 != 0:
            impares += 1
    return impares
for i in range(6):
    numero = int(input(f"numero {i + 1}: "))
    numeros.append(numero)
    quantidadePares = pares(numeros)
    quantidadeImpares = impares(numeros)
print(f"quantidade de pares: {quantidadePares}")
print(f"quantidade de impares: {quantidadeImpares}")