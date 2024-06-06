valor = float(input("valor do produto: "))
print("1-Pagamento à vista")
print("2-Pagamento à prazo")
forma = int(input("forma de pagamento: "))
if forma == 1:
    valormais = valor * 0.1
    pagamento = valor - valormais
    valorDesconto = valormais + valor - valor
    print(f"valor: R$ {valor:.2f}")
    print("forma de pagamento: à vista")
    print(f"valor do desconto: R$ {valorDesconto:.2f}")
    print(f"total a pagar: R$ {pagamento:.2f}")
if forma == 2:
    parcelas = int(input("em quantas parcelas você deseja pagar: "))
    print(f"valor: R$ {valor:.2f}")
    print("forma de pagamento: à prazo")
    print(f"quantidade de parcelas: {parcelas}")
    valorPorParcela = valor / parcelas
    print(f"valor por parcela R$ {valorPorParcela:.2f}")
    print(f"total á prazo: R$ {valor:.2f}")    