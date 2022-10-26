

iPhone = 2980.00
Samsung = 2540.00
Tablet = 1950.00
PS5 = 2100.00
notebook = 2350.00

qtd_iPhone = int(input("Quantos iPhone deseja comprar?"))
qtd_Samsung = int(input("Quantos Sansung deseja comprar?"))
qtd_Tablet = int(input("Quantos Tablets deseja comprar?"))
qtd_PS5 = int(input("Quantos PS5 deseja comprar?"))
qtd_notebook = int(input("“Quantos notebooks deseja comprar?"))

valor = ((iPhone * qtd_iPhone) + (Samsung * qtd_Samsung) + (Tablet * qtd_Tablet) + (PS5 * qtd_PS5) + (notebook * qtd_notebook))
print("O valor total é: ", valor)

valor6 = valor
valor10 = valor

valor = valor/3
print("Valor da parcela dividido em 3X é: ", valor)

valor6 = (((valor6 * (5/100)) + valor6) /6)
print("Valor da parcela dividido em 6X com acréscimo de 5% é: ", valor6)

valor10 = (valor10 - (valor10 * (10/100)))
print("Valor com desconto de 10% para pagamento a vista é: ", valor10)