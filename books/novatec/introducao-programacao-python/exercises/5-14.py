# Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0. No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.
nums = 0
soma = 0
while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break
    nums += 1
    soma += num
print(f"Quantidade de números digitados: {nums}")
print(f"Soma: {soma}")
print(f"Média aritmética: {soma / nums}")