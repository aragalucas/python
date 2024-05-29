a = int(input("digite um numero: "))
b = int(input("digite um numero: "))
operador = input("operador: ")
while operador != "*" and operador != "-" and operador != "+" and operador != "-":
    print("operador invalido")
    operador = input("operador: ")
match(operador):
    case '+':
        resultado = a + b
    case '-':
        resultado = a - b
    case '*':
        resultado = a * b
    case '/':
        resultado = a / b
print(f"resultado: {resultado}")
