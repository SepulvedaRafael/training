'''
158A - PRÓXIMO RODADA (NEXT ROUND)

"Concorrente que ganha uma pontuação igual ou maior do que o ka pontuação do finalizador do último lugar avançará para a próxima rodada, desde que o competidor ganhe uma pontuação positiva..." — um trecho das regras do concurso.

Um total de n os participantes participaram do concurso (n ≥ k), e você já sabe suas pontuações. Calcule quantos participantes avançarão para a próxima rodada.

Entrada
A primeira linha da entrada contém dois inteiros n e k (1 ≤ k ≤ n ≤ 50) separados por um único espaço.

A segunda linha contém n inteiros separados por espaço a1 a2, ..., an (0 ≤ aeu ≤ 100), onde aeu é a pontuação obtida pelo participante que obteve o eu- o lugar. A sequência dada não é crescente (isto é, para todos eu de 1 para n - 1 a seguinte condição é cumprida: aeu ≥ aeu + 1).

Saída
Saída do número de participantes que avançam para a próxima rodada.

Exemplos
Entrada
8 5
10 9 8 7 7 7 5 5
Saída
6
--------------------------
EntradaC
4 2
0 0 0 0
Saída
0

Nota
No primeiro exemplo o participante no 5o lugar ganhou 7 pontos. Como o participante no 6o lugar também ganhou 7 pontos, existem 6 advancers.

No segundo exemplo, ninguém obteve uma pontuação positiva.
'''
contador = 0
n, k = input().split()

n = int(n) # Número de Participantes
k = int(k) # Vagas

participantes = input().split()


for i in participantes:
	i = int(i)

	if(k != 0):
		if(int(participantes[0]) == 0 and int(participantes[n-1]) == 0):
			contador = 0

		elif(int(i == participantes[0]) and int(participantes[n-1]) == i):
			contador += 1

		elif(int(participantes[n-1]) == i and int(participantes[n-1]) != 0):
			contador += 1

		elif(int(participantes[n-1]) != i):
			if(i != 0):
				contador += 1
		k -= 1

	else:
		if(int(participantes[contador-1]) == i and int(participantes[contador-1]) != 0):
			contador += 1

		elif(int(participantes[contador-1]) == i and int(participantes[contador+1]) != i):
					contador += 1
					break

print(contador)