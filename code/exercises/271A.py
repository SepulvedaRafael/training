'''
271A - ANO LINDO (BEAUTIFUL YEAR)

Parece que o ano de 2013 chegou ontem. Você conhece algum fato curioso? O ano de 2013 é o primeiro ano após o antigo 1987 com apenas dígitos distintos.

Agora você é sugerido para resolver o seguinte problema: dado um número de ano, encontrar o número mínimo de ano que é estritamente maior do que o dado e tem apenas dígitos distintos.

Entrada
A linha única contém inteiro y (1000 ≤ y ≤ 9000) — o número do ano.

Saída
Imprimir um único inteiro — o número mínimo do ano que é estritamente maior do que y e todos os seus dígitos são distintos. É garantido que a resposta existe.

Exemplos
Entrada
1987

Saída
2013

-----------
Entrada
2013

Saída
2014
'''
y = int(input())

if(y >= 1000 and y <= 9000):
	ano = y + 1
	ano = str(ano)
	if(sorted(list(ano)) == sorted(set(ano))):
		y = int(y)
		print(ano)
	else:
		while True:
			ano = int(ano)
			ano += 1
			ano = str(ano)

			if(sorted(list(ano)) == sorted(set(ano))):
				print(ano)
				break