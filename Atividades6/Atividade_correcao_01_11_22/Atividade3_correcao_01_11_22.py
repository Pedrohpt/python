# • Numa fazenda em um local reservado para criação coloca-se um casal de coelhos.
# Supondo que em cada mês, a partir do segundo mês de vida, cada casal dá origem a um novo casal de coelhos,
# ao fim de um ano, quantos casais de coelhos estão no pátio?
# Escreva um programa para calcular a quantidade de coelhos em um ano.

def fibonacci(meses):
    if meses > 0 and meses < 3:
        return 1
    else:
        return fibonacci(meses - 1) + fibonacci(meses - 2)

meses = int(input("Digite o número de meses: "))

for i in range(meses):
    casal = fibonacci(i+1)
    print("O numero de casal no mes", i+1, "é", casal)


