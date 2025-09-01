'''
1534 - MATRIZ 123

Leia um valor inteiro N que é o tamanho da matriz que deve ser impressa conforme o modelo fornecido.

Entrada
A entrada contém vários casos de teste e termina com EOF. Cada caso de teste é composto por um único inteiro N (3 ≤ N < 70), que determina o tamanho (linhas e colunas) de uma matriz que deve ser impressa.

Saída
Para cada N lido, apresente a saída conforme o exemplo fornecido.

+------------------------+--------------------------------+
|   Exemplo de Entrada   |       Exemplo de Saída         |
+------------------------+--------------------------------+
|           4            |  1332                          |
|           7            |  3123                          |
|                        |  3213                          |
|                        |  2331                          |
|                        |  1333332                       |
|                        |  3133323                       |
|                        |  3313233                       |
|                        |  3332333                       |
|                        |  3323133                       |
|                        |  3233313                       |
|                        |  2333331                       |
+------------------------+--------------------------------+
'''
while True:
	try:
		n = input()

		for i in range(0, int(n)):
			elemento = ''
			for j in range(0, int(n)):
				if(int(n) % 2 == 0):
					if(i == j):
						elemento += '1'
					elif(i == ((int(n)-1) - j)):
						elemento += '2'
					else:
						elemento += '3'
				else:
					if(i == ((int(n)-1) - j)):
						elemento += '2'
					elif(i == j):
						elemento += '1'
					else:
						elemento += '3'
			print(elemento)
	except EOFError:
		break
