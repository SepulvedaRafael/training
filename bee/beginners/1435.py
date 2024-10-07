'''
1435 - MATRIZ QUADRADA I

Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M de inteiros, e construa a matriz de acordo com o exemplo abaixo.

Entrada
A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas. O final da entrada é marcado por um valor de ordem igual a zero (0).

Saída
Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. Os valores das matrizes devem ser formatados em um campo de tamanho 3 justificados à direita e separados por espaço. Após o último caractere de cada linha da matriz não deve haver espaços em branco. Após a impressão de cada matriz deve ser deixada uma linha em branco.

+------------------------+--------------------------------+
|   Exemplo de Entrada   |       Exemplo de Saída         |
+------------------------+--------------------------------+
|           1            |  1                             |
|           2            |                                |
|           3            |  1  1                          |
|           4            |  1  1                          |
|           5            |                                |
|           0            |  1  1  1                       |
|                        |  1  2  1                       |
|                        |  1  1  1                       |
|                        |                                |
|                        |  1  1  1  1                    |
|                        |  1  2  2  1                    |
|                        |  1  2  2  1                    |
|                        |  1  1  1  1                    |
|                        |                                |
|                        |  1  1  1  1  1                 |
|                        |  1  2  2  2  1                 |
|                        |  1  2  3  2  1                 |
|                        |  1  2  2  2  1                 |
|                        |  1  1  1  1  1                 |
+------------------------+--------------------------------+

elemento = 1
while True:
	n = int(input())

	if(n == 0):
		break
	else:
		for i in range(n):
			for j in range(n):
				if(i >= 1 and i < (n-1) and j > 0 and j < (n-1)):
					print(3*'', elemento+1, end=""),
				else:
					print(3*'', elemento, end="")
			print()
		print()
'''

while True:
	n = int(input())

	if(n == 0):
		break
	else:
		for i in range(1, n+1):
			for j in range(1, n+1):
				elemento = i

				if(j < elemento):
					elemento = j

				if(elemento > (n-i+1)):
					elemento = n-i+1

				if(elemento > (n-j+1)):
					elemento = n-j+1

				print("%3d" % elemento, end='')
				if(j != n):
					print(end=' ')
			print()
		print()