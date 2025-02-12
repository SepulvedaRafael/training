'''
1096 - SEQUÊNCIA IJ 2

Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo

EXEMPLO DE SAÍDA
I=1 J=7
I=1	J=6
I=1	J=5
I=3 J=7
I=3	J=6
I=3	J=5
...
I=9	J=7
I=9	J=6
I=9	J=5
'''
aux = 7
aux2 = 4

for i in range(1, 10, 2):
	for j in range(aux, aux2, -1):
		print(f'I={i} J={j}')
	aux += 2
	aux2 += 2