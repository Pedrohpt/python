#Crie um programa para calcular as notas obtidas pelo aluno do
# ensino médio, deverá mostrar mensagem para ser digitado a
# nota do 1º, 2º, 3º e 4º bimestre. Após deverá mostrar na tela se o aluno foi aprovado, se está em recuperação ou foi reprovado
# sem chance de recuperação.
# Lembrando que cada bimestre vale 25 pontos num total anual de 100 pontos.

print("Programa para calcular notas bimestrais")

b1 = float(input("Digite a nota do 1º bimestre (Valor maximo 25)"))
b2 = float(input("Digite a nota do 2º bimestre (Valor maximo 25)"))
b3 = float(input("Digite a nota do 3º bimestre (Valor maximo 25)"))
b4 = float(input("Digite a nota do 4º bimestre (Valor maximo 25)"))

resultado = b1 + b2 + b3 + b4

if  resultado > 59 and resultado < 101 :
    print("O aluno esta aprovado")
elif resultado >= 40 and resultado < 50 :
    print("O aluno esta em recuperação")
elif resultado < 40 and resultado == 0:
    print("O aluno esta reprovado")
else:
    print("Confirme os valores digitados")