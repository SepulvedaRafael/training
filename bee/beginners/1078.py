'''
1078 - TABUADA

Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:
1 x N = N      2 x N = 2N        ...       10 x N = 10N

Entrada
A entrada contém um valor inteiro N (2 < N < 1000).

Saída
Imprima a tabuada de N, conforme o exemplo fornecido.
'''
x = 1

n = int(input())

if(n >= 2 and n < 1000):
	while(x <= 10):
		print(f'{x} x {n} = {n * x}')

		x += 1