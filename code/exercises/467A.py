'''
467A - GEORGE E ACOMODAÇÕES (GEORGE AND ACCOMMODATION)

George entrou recentemente no BSUCP (Berland State University for Cool Programmers). George tem um amigo Alex que também entrou na universidade. Agora eles estão se mudando para um dormitório.

George e Alex querem morar na mesma sala. O dormitório tem n quartos no total. No momento, o euo quarto tem peu as pessoas que vivem nele e o quarto pode acomodar qeu pessoas no total (peu ≤ qeu). Sua tarefa é contar quantos quartos tem lugar livre para George e Alex.

Entrada
A primeira linha contém um único número inteiro n (1 ≤ n ≤ 100) — o número de quartos.

O eu- o próximo n as linhas contêm dois inteiros peu e qeu (0 ≤ peu ≤ qeu ≤ 100) — o número de pessoas que já vivem no euquarto e a capacidade do quarto.

Saída
Imprimir um único inteiro — o número de quartos onde George e Alex podem se mover.

Exemplos
Entrada
3
1 1
2 2
3 3

Saída
0

------------
Entrada
3
1 10
0 10
10 10

Saída
2
'''
quartos = 0
i = 1

n = int(input())
#p = quantas pessoas vivem no quarto
#q = capacidade do quarto

if(n >= 1 and n <= 100):
	while(i <= n):
		p, q = map(int, input().split())

		if(p >= 0 and q >= 0 and p <= 100 and q <= 100):
			if(p <= q - 2):
				quartos += 1

		i += 1

print(quartos)