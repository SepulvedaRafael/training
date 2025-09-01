# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.
num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
operacao = input("Operação (+, -, * ou /): ")

total = 0
if operacao == "+":
    total = num1 + num2
elif operacao == "-":
    total = num1 - num2
elif operacao == "*":
    total = num1 * num2
elif operacao == "/":
    total = num1 / num2
else:
    print("Operação inválida, digite +, -, * ou /.")
    total = 0
print(f"Resultado da operação ({operacao}): {total}")