# Escreva um programa que leia três números e que imprima o maior eo menor.
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
menor = maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num2 < num3:
    menor = num3
print(f"O menor número digitado foi: {menor}")
print(f"O maior número digitado foi: {maior}")