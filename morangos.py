morangokg = float(input("quantos kilos de morango você quer ?: "))
macakg = float(input("quantos quilos de maçã voce quer ?: "))
frutaskg = macakg + morangokg
if macakg > 5:
    precoMaca = 2.20
else:
    precoMaca = 2.50
if morangokg > 5:
    precoMorango = 1.50
else:
    precoMorango = 1.80
valorMorango = precoMorango * morangokg
valorMaca = macakg * precoMaca
valorCompraSemDesconto = valorMaca + valorMorango
print(f"valor sem desconto: {valorCompraSemDesconto:.2f}")