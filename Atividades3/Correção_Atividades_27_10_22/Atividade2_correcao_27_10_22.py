

tabuada = int(input("Digite o numero da taboada: "))
inicio = int(input("Digite o inicio do intervalo da taboada: "))
fim = int(input("Digite o im do intervalo da taboada: "))

for i in range(inicio,fim+1):
     print("Tabuada do numero:", tabuada, "resultado,", tabuada, "*", i, "=",  tabuada * i)