# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário  e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
valor_salario = float(input("Salário: R$"))
porcentagem_aumento = int(input("Aumento (%): "))
aumento = (valor_salario * porcentagem_aumento) / 100
print(f"Aumento: R${aumento:5.2f}")
print(f"Novo salário: R${valor_salario + aumento:5.2f}")