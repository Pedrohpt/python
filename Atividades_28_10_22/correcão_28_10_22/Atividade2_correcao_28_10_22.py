# • Crie um programa para calcular as notas obtidas pelo aluno do
# ensino médio, deverá mostrar mensagem para ser digitado a
# nota da 1ª, 2ª, 3ª e 4ª prova e a nota do 1º, 2º, 3º e 4º trabalho. Após deverá mostrar na tela a média obtida no 1º, 2º, 3º e 4º
# bimestre.
# • E depois o total informado se o aluno foi aprovado, esta em
# recuperação ou foi reprovado sem recuperação.

p1 = float(input("Digite a nota do 1º bimestre (Valor maximo 25)"))
t1 = float(input("Digite a nota do 1º bimestre (Valor maximo 25)"))
p2 = float(input("Digite a nota do 2º bimestre (Valor maximo 25)"))
t2 = float(input("Digite a nota do 2º bimestre (Valor maximo 25)"))
p3 = float(input("Digite a nota do 3º bimestre (Valor maximo 25)"))
t3 = float(input("Digite a nota do 3º bimestre (Valor maximo 25)"))
t4 = float(input("Digite a nota do 4º bimestre (Valor maximo 25)"))
p4 = float(input("Digite a nota do 4º bimestre (Valor maximo 25)"))


b1 = (p1 + t1) /2
b2 = (p2 + t2) /2
b3 = (p3 + t3) /2
b4 = (p4 + t4) /2

print("A media do 1º bimestre é:", b1)
print("A media do 2º bimestre é:", b2)
print("A media do 3º bimestre é:", b3)
print("A media do 4º bimestre é:", b4)

resultado = b1 + b2 + b3 + b4

if  resultado > 59 and resultado < 101 :
    print("O aluno esta aprovado")
elif resultado >= 40 and resultado < 50 :
    print("O aluno esta em recuperação")
elif resultado < 40 and resultado == 0:
    print("O aluno esta reprovado")
else:
    print("Confirme os valores digitados")