'''
1099 - SOMA DE ÍMPARES CONSECUTIVOS II

Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.

+------------------------+----------------------+
|   Exemplo de Entrada   |   Exemplo de Saída   |
+------------------------+----------------------+
|           7            |           0          |
|          4 5			 |		    11          |
|         13 10			 |			 5          |
|          6 4			 |           0          |
|          3 3			 |           0          |
|          3 5			 |           0          |
|          3 4			 |           12         |
|          3 8			 |                      |
+------------------------+----------------------+
'''
lista = []

n = int(input())

for i in range(1, n+1):
	x, y = input().split()

	x = int(x)
	y = int(y)
	soma = 0

	if(x > y):
		for j in range(x, y, -1):
			if(j != x and j != y):
				if((j % 2) != 0):
					soma += j
			else:
				soma += 0
		lista.append(soma)
	elif(x == y):
		lista.append(0)
	else:
		for j in range(x, y, 1):
			if(j != x and j != y):
				if((j % 2) != 0):
					soma += j
			else:
				soma += 0
		lista.append(soma)

for k in lista:
	print(k)
