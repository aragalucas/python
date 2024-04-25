numeroUm = int(input("digite o numero um: "))
numeroDois = int(input("digite o numero dois: "))
soma = numeroUm + numeroDois
media = soma / 2
produto = numeroDois * numeroUm
if numeroUm < numeroDois:
    print("numero um é menor")
    print("numero dois é maior")
else:
    print("numero um é maior")
    print("numero dois é menor")