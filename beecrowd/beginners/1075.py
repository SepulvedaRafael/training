'''
1075 - RESTO 2

Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.

Entrada
A entrada contém um valor inteiro N (N < 10000).

Saída
Imprima todos valores que quando divididos por N dão resto = 2, um por linha.
'''
x = 0

n = int(input())

if(n < 10000):
	while(x < 10000):
		if((x % n) == 2):
			print(x)
		x += 1