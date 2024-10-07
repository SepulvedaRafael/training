'''
1094 - EXPERIÊNCIAS

Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.
'''
cobaias = {}
x = 0
totalCobaias = 0

n = int(input())

while(x < n):
	quantia = input().split(" ")

	if(quantia[1] in cobaias.keys()):
		cobaias[quantia[1]] = int(cobaias.get(quantia[1])) + int(quantia[0])
	else:
		cobaias[quantia[1]] = quantia[0]

	x += 1

for cobaia in cobaias:
	totalCobaias += int(cobaias.get(cobaia))

coelhos = int(cobaias.get('C'))
ratos = int(cobaias.get('R'))
sapos = int(cobaias.get('S'))

print(f'Total: {totalCobaias} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {(((totalCobaias + coelhos) / totalCobaias - 1) * 100):.2f} %')
print(f'Percentual de ratos: {(((totalCobaias + ratos) / totalCobaias - 1) * 100):.2f} %')
print(f'Percentual de sapos: {(((totalCobaias + sapos) / totalCobaias - 1) * 100):.2f} %')