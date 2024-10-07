'''
1064 - POSITIVOS E MÉDIA

Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.
'''
i = 1
contador = 0
soma = 0

while (i <= 6):
	valor = float(input())

	if(valor > 0):
		soma += valor
		contador += 1
	i += 1

media = soma / contador

print(f'{contador} valores positivos')
print(f'{media:.1f}')