# Faça um programa para imprimir igual abaixo:
# 1
# 2 2
# 3 3 3 ...
# n n n n ...
# “n” para um ”numero” (range) informado pelo usuário.
# • Use uma função que receba um valor n inteiro e imprima até a “n-Linha” informada pelo usuário.

def repeticao(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i, end="")
        print("\r")


n = int(input("Digite um numero inteiro: "))

repeticao(n)