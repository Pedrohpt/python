# • Numa fazenda em um local reservado para criação coloca-se um casal de coelhos.
# Supondo que em cada mês, a partir do segundo mês de vida, cada casal dá origem a um novo casal de coelhos,
# ao fim de um ano, quantos casais de coelhos estão no pátio?
# Escreva um programa para calcular a quantidade de coelhos em um ano.


def fibonacci(n):
    if n > 0 and n < 3:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 12

print("“Ao final de um ano" ,fibonacci(n), "casais de coelhos estaram no patio")