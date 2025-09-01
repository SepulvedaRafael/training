# Escreva um programa que leia um número e verifique se é ou não um número primo. Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.
num = int(input("Digite um número: "))

if num >= 2:
    div = 0
    x = 2
    while x <= num:
        if num % x == 0:
            div += 1
        x += 1
    if div == 1:
        print("É um número primo!")
    else:
        print("Não é um número primo!")
else:
    print("Não é um número primo!")