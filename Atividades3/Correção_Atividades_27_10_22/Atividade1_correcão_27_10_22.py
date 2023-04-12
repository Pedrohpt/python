
print("Programa para realizar saudação do dia")
turno = input("Digite seu turno, M para manhã, T para tarde e N para noite").upper()

match turno:
    case "M":
        print("Bom dia")
    case "T":
        print("Boa tarde")
    case "N":
        print("Boa tarde")
    case _:
        print("Valor invalido")