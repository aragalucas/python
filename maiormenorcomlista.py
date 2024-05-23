numeros = []
maiorNumero = 0
menorNumero = 2000000
QUANTIDADE_NOTAS = 5
for i in range(QUANTIDADE_NOTAS):
    numero = float(input(f"digite o numero {i + 1}: "))
    numeros.append(numero)
    if numero > maiorNumero:
        maiorNumero = numero
    if numero < menorNumero:
        menorNumero = numero
print(f"maior numero {maiorNumero}")
print(f"menor numrero {menorNumero}")
for i in range(QUANTIDADE_NOTAS):
    print(f"numero {i + 1}: {numeros[i]}")