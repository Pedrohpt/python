# • Crie um programa em que o usuário deve digitar números
# inteiros para uma matriz de 5 linhas e 5 colunas .
# • Após a digitação dos números, o usuário deve digitar um número aleatório e verificar se ele se encontra na matriz.
# • Ao final, os índices da linha e da coluna devem ser impressos se o elemento for encontrado; caso contrário, a mensagem “elemento não encontrado” deve ser mostrada na tela.

m = [[0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4]]

msg = False

for i in range(5):
    for j in range(5):
        m[i][j] = int(input("Preencha a matriz com um numero inteiro: "))

num = int(input("Digite um numero interiro para localizar na matriz: "))

for i in range(5):
    for j in range(5):
        if m[i][j] == num:
            print("Numero", num, "encontrado na posição", i, j)
            msg = True


if msg is False:
    print("Numero", num, "não encontrado")
