'''
1155 - SEQUÊNCIA S

Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
S = 1 + 1/2 + 1/3 + … + 1/100

Entrada
Não há nenhuma entrada neste problema.

Saída
A saída contém um valor correspondente ao valor de S.
O valor deve ser impresso com dois dígitos após o ponto decimal.
'''
s = 0
n = 1

for i in range(1, 40, 2):
	s += i/n
	n *= 2
print(f'{s:.2f}')