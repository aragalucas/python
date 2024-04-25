nome = input("nome do produto: ")
quantidade = int(input("quantidade: "))
preco = int(input("preço unitario: "))
total = quantidade * preco
if quantidade <= 5:
    desconto = 2
elif quantidade > 5 and quantidade <= 10:
    desconto = 3
elif quantidade > 10:
    desconto = 5
pagar = total - desconto
print(f"total: {total}")
print(f"desconto: {desconto}")
print(f"total a pagar {pagar}")