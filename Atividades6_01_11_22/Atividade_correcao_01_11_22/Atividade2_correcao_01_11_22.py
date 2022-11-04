# Faça um programa para imprimir igual abaixo:
# 1
# 2 2
# 3 3 3 ...
# n n n n ...
# “n” para um ”numero” (range) informado pelo usuário.
# • Use uma função que receba um valor n inteiro e imprima até a “n-Linha” informada pelo usuário.

numero = int(input("Digite um numero inteiro para exibir for alinhado: "))

for i in range(numero):
    for j in range(i+1):
        print(i+1, end=" ")
    print("")