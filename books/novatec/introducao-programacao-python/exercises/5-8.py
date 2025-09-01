# Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 x 5 = 5 + 5 + 5 + = 4 + 4 + 4 + 4 + 4.
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

x = 1
result = 0
while x <= num2:
    result += num1
    x += 1
print(f"O resultado da multiplicação é: {result}")