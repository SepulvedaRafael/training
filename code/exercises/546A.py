'''
546A - SOLDADO E BANANAS (SOLDIER AND BANANAS)

Um soldado quer comprar w bananas na loja. Ele tem que pagar k dólares para a primeira banana, por exemplo 2k dólares para o segundo e assim por diante (em outras palavras, ele tem que pagar euék dólares para o eu- a banana).

Ele tem n dólares. Quantos dólares ele tem que emprestar de seu amigo soldado para comprar w bananas?

Entrada
A primeira linha contém três inteiros positivos k n w (1 ≤  k w  ≤ 1000 0 ≤ n ≤ 109), o custo da primeira banana, o número inicial de dólares que o soldado tem e o número de bananas que ele quer.

Saída
Saída de um inteiro — a quantidade de dólares que o soldado deve emprestar de seu amigo. Se ele não tem que pedir dinheiro emprestado, saída 0.

Exemplos
Entrada
3 17 4

Saída
13
'''
total = 0
k, n, w = map(int, input().split())

for i in range(1, w+1):
	total += i * k

if(total <= n):
	print(0)
else:
	print(total - n)