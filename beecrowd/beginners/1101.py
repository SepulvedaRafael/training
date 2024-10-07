'''
1101 - SEQUÊNCIA DE NÚMEROS E SOMA

Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

+------------------------+----------------------+
|   Exemplo de Entrada   |   Exemplo de Saída   |
+------------------------+----------------------+
|          5 2           |    2 3 4 5 Sum=14    |
|          6 3			 |	  3 4 5 6 Sum=18    |
|          5 0			 |			            |
+------------------------+----------------------+
'''
while True:
	m, n = input().split()

	m = int(m)
	n = int(n)

	if(m <= 0 or n <= 0):
		break
	else:
		if(m > n):
			aux = 0
			for i in range(n, m+1):
				aux += i
				print(i, end=" ")
			print(f'Sum={aux}')
		else:
			aux = 0
			for i in range(m, n+1):
				aux += i
				print(i, end=" ")
			print(f'Sum={aux}')