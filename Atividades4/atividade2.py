# • Crie um programa para calcular as notas obtidas pelo aluno do
# ensino médio, deverá mostrar mensagem para ser digitado a
# nota da 1ª, 2ª, 3ª e 4ª prova e a nota do 1º, 2º, 3º e 4º trabalho. Após deverá mostrar na tela a média obtida no 1º, 2º, 3º e 4º
# bimestre.
# • E depois o total informado se o aluno foi aprovado, esta em
# recuperação ou foi reprovado sem recuperação.

pro1 = float(input("Digite a nota da prova do primeiro bimestre: "))
pro2 = float(input("Digite a nota da prova do segundo bimestre: "))
pro3 = float(input("Digite a nota da prova do terceiro bimestre: "))
pro4 = float(input("Digite a nota da prova do quarto bimestre: "))

tra1 = float(input("Digite a nota do trabalho do primeiro bimestre: "))
tra2 = float(input("Digite a nota do trabalho do segundo bimestre: "))
tra3 = float(input("Digite a nota do trabalho do terceiro bimestre: "))
tra4 = float(input("Digite a nota do trabalho do quarto bimestre: "))

total = pro1 + pro2 + pro3 + pro4 + tra1 + tra2 + tra3 + tra4

print("Sua nota no primeiro bimestre:", (pro1 + pro2)/2)
print("Sua nota no segundo bimestre:", (pro1 + pro2)/2)
print("Sua nota no terceiro bimestre:", (pro1 + pro2)/2)
print("Sua nota no quarto bimestre:", (pro1 + pro2)/2)

if  total >= 60 and total <= 100:
    print("Nota total:", total, "Aluno Aprovado")
elif total >= 40 and total < 60:
    print("Nota total:", total, "Aluno em Recuperação")
elif total < 40 and total >= 0:
    print("Nota total:", total, "Aluno Reprovado")
else:
    print("Nota não aceita")