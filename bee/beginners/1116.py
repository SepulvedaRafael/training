'''
1116 - DIVIDINDO X POR Y

Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo. Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.

Entrada
A entrada contém um número inteiro N. Este N será a quantidade de pares de valores inteiros (X e Y) que serão lidos em seguida.

Saída
Para cada caso mostre o resultado da divisão com um dígito após o ponto decimal, ou “divisao impossivel” caso não seja possível efetuar o cálculo.

Obs.: Cuide que a divisão entre dois inteiros em algumas linguagens como o C e C++ gera outro inteiro. Utilize cast :)

+------------------------+----------------------+
|   Exemplo de Entrada   |   Exemplo de Saída   |
+------------------------+----------------------+
|         2  2           |         -1.5         |
|         3 -2			 |	divisao impossivel  |
|        -8 -1			 |          0.0         |
|        -7  1			 |                      |
+------------------------+----------------------+
'''
i = 0
n = int(input())

while(i < n):
	x, y = map(int, input().split())

	if(x <= 0 and y == 0):
		print('divisao impossivel')
	else:
		if(y == 0):
			print('divisao impossivel')
		else:
			z = x / y
			print(f'{z:.1f}')

	i += 1