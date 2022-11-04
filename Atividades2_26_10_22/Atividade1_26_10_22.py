
iPhone = 2980
Samsung = 2540
Tablet = 1950
PS5 = 2100
notebook = 2350

qtd_iPhone = int(input("Preço iPhone: 2980. Quantos iPhone deseja comprar? "))
qtd_Samsung = int(input("Preço Samsung: 2540. Quantos Sansung deseja comprar? "))
qtd_Tablet = int(input("Preço Tablet: 1950. Quantos Tablets deseja comprar? "))
qtd_PS5 = int(input("Preço PS5: 2100. Quantos PS5 deseja comprar? "))
qtd_notebook = int(input("Preço notebook: 2350. Quantos notebooks deseja comprar? "))

valor = ((iPhone * qtd_iPhone) + (Samsung * qtd_Samsung) + (Tablet * qtd_Tablet) + (PS5 * qtd_PS5) + (notebook * qtd_notebook))
print("O valor total é: R$", valor)

valor3 = valor/3
print("Valor da parcela dividido em 3X é: R$", valor3)

valor6 = (((valor * (5/100)) + valor) /6)
print("Valor da parcela dividido em 6X com acréscimo de 5% é: R$", valor6)

valor10 = (valor - (valor * (10/100)))
print("Valor com desconto de 10% para pagamento a vista é: R$", valor10)