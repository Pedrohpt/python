# • Faça um Programa que leia em um vetor de 10 caracteres (letras ) e diga quantas consoantes foram lidas.
# • Mostre as consoantes.

letra = [0,0,0,0,0,0,0,0,0,0]
#["b","c","d","f","g","h","j","k","l","m","n","o","p","q","r","s","t","v","w","x","y","z"]

num = 0

for i in range(10):
    letra[i] = str(input("Digite uma letra: ")).upper()

for i in range(10):
    if letra[i] != "A" and letra[i] != "E" and letra[i] != "I" and letra[i] != "O" and letra[i] != "U":
        print(letra[i], end="")
        num = num + 1
print("\r")
print(num, "consoantes")