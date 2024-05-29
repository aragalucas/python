dia = int(input("numero: "))
match(dia):
    case 1:
        util = "final de semana"
    case 2:
        util = "dia util"
    case 3:
        util = "dia util"
    case 4:
        util = "dia util"
    case 5:
        util = "dia util"
    case 6:
        util = "dia util"
    case 7:
        util = "final de semana"
    case _:
        util = "invalido"
print(f"o dia é {util}")