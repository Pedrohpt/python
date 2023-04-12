# Crie um programa com uma função para multiplicar dois números e o algoritmo mostrar o resultado.


def multiplicar(num1,num2):
    result = num1 * num2

    return result

print("Programa para multiplicar numeros")
num1 = float(input("Escreva o primeiro numero: "))
num2 = float(input("Escreva o segundo numero: "))


print(num1, "*", num2, "=", multiplicar(num1,num2))