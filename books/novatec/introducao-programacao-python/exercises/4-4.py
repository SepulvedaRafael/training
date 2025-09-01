# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salário superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
salario = float(input("Salário do funcionário: "))
aumento = 0.15
if salario > 1250:
    aumento = 0.10
print(f"Novo salário: R${salario + (salario * aumento):5.2f}")