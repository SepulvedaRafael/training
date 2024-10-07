'''
1071 - SOMA DE IMPARES CONSECUTIVOS I

Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.
'''
soma = 0

x = int(input())
y = int(input())

if(x > y):
	if((x % 2) != 0):
		x -= 1
		while(x > y):
			if((x % 2) != 0):
				soma += x
			x -= 1
	else:
		while(x > y):
			if((x % 2) != 0):
				soma += x
			x -= 1
elif(x == y):
	if((x % 2) != 0):
		soma += x
else:
	while(y > x):
		if((y % 2) != 0):
			soma += x
		y -= 1

print(soma)