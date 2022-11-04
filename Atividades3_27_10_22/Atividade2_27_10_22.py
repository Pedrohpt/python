
num1 = int(input("Escreva um número inteiro que deseja saber a tabuada: "))
inicio = int(input("Escreva o número inicial do intervalo da tabuada: "))
fim = int(input("Escreva o número final do intervalo da tabuada: "))

i = inicio
for i in range(inicio, fim +1):
    print(str(num1), "*", str(i),"=", int(num1) * i)