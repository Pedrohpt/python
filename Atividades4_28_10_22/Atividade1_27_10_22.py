# Crie um programa para calcular as notas obtidas pelo aluno do
# ensino médio, deverá mostrar mensagem para ser digitado a
# nota do 1º, 2º, 3º e 4º bimestre. Após deverá mostrar na tela se o aluno foi aprovado, se está em recuperação ou foi reprovado
# sem chance de recuperação.
# Lembrando que cada bimestre vale 25 pontos num total anual de 100 pontos.


print("Programa para calcular as notas do aluno")

nota1 = float(input("Digite a sua nota no primeiro bimestre: "))
nota2 = float(input("Digite a sua nota no segundo bimestre: "))
nota3 = float(input("Digite a sua nota no terceiro bimestre: "))
nota4 = float(input("Digite a sua nota no quarto bimestre: "))

total = nota1 + nota2 + nota3 + nota4

if  total >= 60 and total <= 100:
    print("Nota total:", total, "Aluno Aprovado")
elif total >= 40 and total < 60:
    print("Nota total:", total, "Aluno em Recuperação")
elif total < 40 and total >= 0:
    print("Nota total:", total, "Aluno Reprovado")
else:
    print("Nota não aceita")