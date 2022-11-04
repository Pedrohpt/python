# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, mostre todos os descontos, mostre o salário bruto e o líquido.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# • Salário Bruto : R$ - IR (11%) : R$ - INSS (8%) : R$ - Sindicato ( 5%)
# • Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

valor = float(input("Dite o numero de horas trabalhadas: "))
hora = float(input("Digite o numero de horas trabalhadas no mes: "))

salarioBruto = valor * hora
inss = salarioBruto * 0.11
ir = salarioBruto * 0.08
sindicato = ir * 0.05

salarioLiquido = salarioBruto - inss - ir - sindicato

print("Salario bruto: ", round(salarioBruto,2))
print("Desconto INSS: ", round(inss,2))
print("Desconto Imposto de Renda: ", round(ir,2))
print("Desconto sindicato", round(sindicato,2))
print("Seu salario liquido é: ", round(salarioLiquido,2))