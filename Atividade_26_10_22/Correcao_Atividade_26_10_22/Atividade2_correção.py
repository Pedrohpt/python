
print("Programa adivinha número inteiro")

num1= int(input("Digite um numero inteiro"))

if num1 > 10:
    print("O numero digitado é maior que o numero secreto")
elif num1 < 10:
    print("O numero digitado é menor que o numero secreto")
else:
    print("Acertou o numero secreto")