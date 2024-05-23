def inflacao(valor):
    valorfinal = 0
    if valor < 100:
        valormeio = valor * 0.1
        valorfinal = valor + valormeio
    elif valor >= 100:
        valormeio = valor * 0.2
        valorfinal = valor + valormeio
    return valorfinal
preco = int(input("preço: "))
inflacionado = inflacao(preco)
print(f"valor inflacionado {inflacionado}")