# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
preco_mercadoria = float(input("Preço da mercadoria: R$"))
percentual_desconto = int(input("Desconto (%): "))
desconto = (preco_mercadoria * percentual_desconto) / 100
print(f"Desconto: R${desconto:5.2f}")
print(f"Preço a pagar: R${preco_mercadoria - desconto:5.2f}")