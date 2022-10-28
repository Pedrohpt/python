reset = "S"

while reset == "S":

    num1 = float(input("Digite um numero: "))
    sinal = str(input("Digite o sinal da conta: "))
    num2 = float(input("Digite um numero: "))

    if sinal == "+":
        print(num1, "+", num2, "=", num1 + num2)
    elif sinal == "-":
        print(num1, "-", num2, "=", num1 - num2)
    elif sinal == "*":
        print(num1, "*", num2, "=", num1 * num2)
    elif sinal == "/":
        print(num1, "/", num2, "=", num1 / num2)
    else:
        print("ERRO")

    reset = input('''Deseja continuar utilizando a calculadora?
Digite S para sim ou N para não. ''')

    if reset == "s":
        reset = "S"
    elif reset == "S":
        reset == "S"
    else:
        print("Ate mais")