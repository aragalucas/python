numeroUm = int(input("digite o numero um: "))
numeroDois = int(input("digite o numero dois: "))
soma = numeroUm + numeroDois
media = soma / 2
produto = numeroDois * numeroUm
print(f"media: {media}")
print(f"soma: {soma}")
print(f"produto: {produto}")
if numeroUm < numeroDois:
    print("numero um é menor")
    print("numero dois é maior")
else:
    print("numero um é maior")
    print("numero dois é menor")