import os
# função sem retorno
def logosenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")
    
#função com retorno
def somar(n1, n2):
    resultado = n1 + n2
    return resultado

logosenai()
nome = input("nome: ")
logosenai()
idade = int(input("idade: "))
logosenai()
primeiroNumero = int(input("numero 1: "))
logosenai()
segundoNumero = int(input("numero 2: "))
soma = somar(primeiroNumero, segundoNumero)
logosenai()
print(f"soma: {soma}")