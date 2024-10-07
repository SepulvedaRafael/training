'''
1187 - ÁREA SUPERIOR

Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão na área superior da matriz, conforme ilustrado abaixo (área verde).

Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem 144 valores com ponto flutuante de dupla precisão que compõem a matriz.

Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

+------------------------+--------------------------------+
|   Exemplo de Entrada   |       Exemplo de Saída         |
+------------------------+--------------------------------+
|           S            |             112.4              |
|          1.0           |                                |
|        330.0           |                                |
|         -3.5           |                                |
|          2.5           |                                |
|          4.1           |                                |
|          ...           |                                |
+------------------------+--------------------------------+
'''
o = input()

soma = 0
media = 0
contador = 0
first = 0
last = 11
for i in range(12): # Linha
	for j in range(12): # Coluna
		value = float(input())

		if(last != j and first != j and last > j and first < j):
			if(o == 's' or o == 'S'):
				soma += value
			elif(o == 'm' or o == 'M'):
				soma += value
			contador += 1
	first += 1
	last -= 1

if(o == 'm' or o == 'M'):
	media = soma / contador
	print(f'{media:.1f}')
elif(o == 's' or o == 'S'):
	print(f'{soma:.1f}')