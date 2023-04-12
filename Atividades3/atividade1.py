
turno = input("Digite a letra respectiva ao turno que você estuda. M-Matutino, V-Vespertino ou N-Noturno:  ").upper()

match turno:
    case "M":
        print("Bom dia")
    case "V":
        print("Boa tarde")
    case "N":
        print("Boa noite")
    case _:
        print("Valor invalido")