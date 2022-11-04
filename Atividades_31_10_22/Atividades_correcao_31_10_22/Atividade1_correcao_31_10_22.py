# • Faça um Programa que leia em um vetor de 10 caracteres (letras ) e diga quantas consoantes foram lidas.
# • Mostre as consoantes.

vetor = []

for i in range(10):
    consoante = (input("Digite uma letra de A - Z: "))
    if consoante not in ["a","e","i","o","u"]:
        vetor.append(consoante)

print("O vetor possui", len(vetor), "posições de consoantes lidas")
print("Consoantes digitadas", vetor)