# • Crie um programa em que o usuário deve digitar números
# inteiros para uma matriz de 5 linhas e 5 colunas .
# • Após a digitação dos números, o usuário deve digitar um número aleatório e verificar se ele se encontra na matriz.
# • Ao final, os índices da linha e da coluna devem ser impressos se o elemento for encontrado; caso contrário, a mensagem “elemento não encontrado” deve ser mostrada na tela.

m = [[0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4]]

msg = False

for i in range(5):
    for j in range(5):
        m[i][j] = int(input("Preencha a matriz: "))

num = int(input("Digite um numero: "))

for i in range(5):
    for j in range(5):
        if m[i][j] == num:
            msg = True


if msg == False:
    print("Numero não encontrado")
else :
    print("Você acertou é: ", m[i][j])