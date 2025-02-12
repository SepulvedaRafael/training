'''
1189 - ÁREA ESQUERDA

Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão na área esquerda da matriz, conforme ilustrado abaixo (área verde).

Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

+------------------------+--------------------------------+
|   Exemplo de Entrada   |       Exemplo de Saída         |
+------------------------+--------------------------------+
|           S            |             111.4              |
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
		# 11 != 0 and 0 != 0 and 0 >= 0 and 11 < 0
		if(last != j and first != j and last > j and first >= j):
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