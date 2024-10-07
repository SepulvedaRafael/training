'''
1018 - CÉDULAS

Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
'''
valor = int(input())

print(valor)
notas = valor // 100
print(f"{notas} nota(s) de R$ 100,00")
valor = valor % 100

notas = valor // 50
print(f"{notas} nota(s) de R$ 50,00")
valor = valor % 50

notas = valor // 20
print(f"{notas} nota(s) de R$ 20,00")
valor = valor % 20

notas = valor // 10
print(f"{notas} nota(s) de R$ 10,00")
valor = valor % 10

notas = valor // 5
print(f"{notas} nota(s) de R$ 5,00")
valor = valor % 5

notas = valor // 2
print(f"{notas} nota(s) de R$ 2,00")
valor = valor % 2

notas = valor // 1
print(f"{notas} nota(s) de R$ 1,00")
valor = valor % 1