"""
EXTRA: 
se a idade inserida for negativa, repita a pergunta
se o salario inserido tiver um valor negativo, repita a pergunta
se o cacarter de sexo for invalido (!= M or F) repita a pergunta
"""
print("codigo| descrição")
print("  1   | adicionar pessoa")
print("  2   | exibir resultados e sair")
codigo = int(input("codigo: "))
salarioGeral = 0
mulheres5k = 0
maiorIdade = 0
menorIdade = 500
vezes = 0
while codigo != 2:
    idade = int(input("idade: "))
    while idade < 0:
        idade = int(input("idade: "))
    sexo = input("sexo: ")
    while sexo != "M" and sexo != "F":
        sexo = input("sexo: ")
    salario = int(input("salario: "))
    while salario < 0:
        salario = int(input("salario: "))
    codigo = int(input("codigo: "))
    salarioGeral += salario
    if idade < menorIdade:
        menorIdade = idade
    if idade >maiorIdade:
        maiorIdade = idade
    if sexo == "M" and salario >= 5000:
        mulheres5k += 1
    vezes += 1
media = salarioGeral / vezes
print(f"media dos salarios: {media}")
print(f"maior idade: {maiorIdade}")
print(f"menor idade: {menorIdade}")
print(f"quantidade de mulheres com mais de 5 mil de salario: {mulheres5k}")