# Faça um programa que calcule o fatorial de um número, é obrigatório o uso de função recursiva para o calculo fatorial.

def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num-1)

num = int(input("Digite um numero: "))

print("Fatorial de", num)

for i in range(num):
    n = fatorial(i+1)
    print(i+1,"-", n)