'''
1178 - PREENCHIMENTO DE VETOR III

Leia um valor X. Coloque este valor na primeira posição de um vetor N[100]. Em cada posição subsequente de N (1 até 99), coloque a metade do valor armazenado na posição anterior, conforme o exemplo abaixo. Imprima o vetor N.

Entrada
A entrada contem um valor de dupla precisão com 4 casas decimais.

Saída
Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela posição. Cada valor do vetor deve ser apresentado com 4 casas decimais.

+------------------------+--------------------------------+
|   Exemplo de Entrada   |       Exemplo de Saída         |
+------------------------+--------------------------------+
|        200.000         |         N[0] = 200.0000        |
|                        |         N[0] = 100.0000        |
|                        |         N[0] = 50.0000         |
|                        |         N[0] = 25.0000         |
|                        |         N[0] = 12.5000         |
|                        |               ...              |
+------------------------+--------------------------------+
'''
x = float(input())

for i in range(100):
	print(f'N[{i}] = {x:.4f}')
	x /= 2