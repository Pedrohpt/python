# • Crie um programa que leia um conjunto de nomes de 20 estudantes
# inscritos na prova do ENEM. Com esses nomes, realizar uma
# ordenação crescente usando uma função para facilitar a localização
# do nome na lista que será afixada no quadro de avisos da escola.

nome = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))

for i in range(20):
     nome[i] = str(input("Digite um nome: "))

print(quicksort(nome))


# for i in range(3):
#     print(quicksort(my_list))