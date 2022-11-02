# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, mostre todos os descontos, mostre o salário bruto e o líquido.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# • Salário Bruto : R$ - IR (11%) : R$ - INSS (8%) : R$ - Sindicato ( 5%)
# • Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

salario = float(input("Digite quanto você ganha por hora: "))
horas =  float(input("Digite o numero de horas trabalhadas no mês: "))

bruto = salario * horas
ir = (bruto - (bruto * (11/100)))
inss = (ir - (ir * (8/100)))
sindicato = (inss - (inss * (5/100)))
liquido = sindicato

print("Salario bruto: R$",bruto)
print("Salario liquido: R$",liquido)
print("Quanto pagou ao INSS: R$",bruto - ir)
print("Quanto pagou ao INSS: R$",ir - inss)
print("Quanto pagou ao Sindicato: R$",inss - sindicato)