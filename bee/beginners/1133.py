'''
1133 - RESTO DA DIVISÃO

Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.

Entrada
O arquivo de entrada contém 2 valores positivos inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.

+------------------------+--------------------------------+
|   Exemplo de Entrada   |       Exemplo de Saída         |
+------------------------+--------------------------------+
|         10             |                12              |
|         18			 |                13              |
|           			 |                17              |
+------------------------+--------------------------------+
'''
x = int(input())
y = int(input())

valores = []

if (x >= 0 and y >= 0):
	if(x > y):
		for i in range(y+1, x):
			if((i % 5) == 2 or (i % 5) == 3):
				valores.append(i)
	else:
		for i in range(x+1, y):
			if(i % 5 == 2 or i % 5 == 3):
				valores.append(i)

valores.sort()

for j in valores:
	print(j)
