notas = []

for i in range(3):
    nota = float(input(f"digite a nota {i + 1}: "))
    notas.append(nota)
for i in range(3):
    print(f"Nota {i + 1}: {notas[i]}")