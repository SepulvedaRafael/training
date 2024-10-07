'''
1098 - SEQUÊNCIA IJ 4

Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.

EXEMPLO DE SAÍDA
I=0 J=1
I=0	J=2
I=0	J=3
I=0.2 J=1.2
I=0.2	J=2.2
I=0.2	J=3.2
...
I=2	J=?
I=2	J=?
I=2	J=?
'''
contador = 0

irange = (i / 5 for i in range(0, 11))

for i in irange:
	for j in range(1, 4):
		if(i == 0 or i == 1):
			print(f'I={i:.0f} J={j+i:.0f}')
		elif(contador == 10):
			print(f'I={i:.0f} J={j+i:.0f}')
		else:
			print(f'I={i:.1f} J={j+i:.1f}')

	contador += 1