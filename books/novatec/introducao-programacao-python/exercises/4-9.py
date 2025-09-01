# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar divido pelo número de meses a pagar.
valor_casa = float(input("Valor da casa a pagar: R$"))
salario = float(input("Salário: R$"))
quantidade_anos = int(input("Quantidade de anos a pagar: "))
valor_prestacao = valor_casa / (quantidade_anos * 12)
if valor_prestacao > salario * 0.3:
    print("A prestação é superior a 30% do seu salário!")
else:
    print("Empréstimo aprovado!")
    print(f"O valor da prestação mensal é: R${valor_prestacao:5.2f}")