'''
50A - ESTACAS DOMINO (DOMINO PILING)

Você recebe uma placa retangular de M × N quadrados. Além disso, você recebe um número ilimitado de peças de dominó padrão de 2 × 1 quadrados. Você pode girar as peças. Você é solicitado a colocar o maior número possível de dominós no tabuleiro para atender às seguintes condições:

1. Cada dominó cobre completamente dois quadrados.

2. Não há dois dominós sobrepostos.

3. Cada dominó fica inteiramente dentro do tabuleiro. É permitido tocar as bordas da placa.

Encontre o número máximo de dominós, que podem ser colocados sob essas restrições.

Entrada
Em uma única linha, você recebe dois inteiros M e N — tamanhos de pranchas em quadrados (1 ≤ M ≤ N ≤ 16).

Saída
Saída de um número — o número máximo de dominós, que pode ser colocado.

Exemplos
Entrada
2 4
Saída
4
------------
Entrada
3 3

Saída
4
'''
pecas = 0
m, n = input().split()

m = int(m)
n = int(n)

matriz = m * n

if((matriz % 2) == 0):
	pecas = matriz / 2
else:
	pecas = matriz / 2

print(int(pecas))