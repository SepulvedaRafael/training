'''
263A - BELA MATRIX (BEAUTIFUL MATRIX)

Você tem um 5 × 5 matriz, constituída por 24 zeros e um único número um. Vamos indexar as linhas da matriz por números de 1 para 5 de cima para baixo, vamos indexar as colunas da matriz por números de 1 para 5 da esquerda para a direita. Em um movimento, você pode aplicar uma das duas transformações a seguir à matriz:

Troque duas linhas de matriz vizinhas, ou seja, linhas com índices eu e eu + 1 para algum inteiro eu (1 ≤ eu < 5).
Troque duas colunas de matriz vizinhas, isto é, colunas com índices j e j + 1 para algum inteiro j (1 ≤ j < 5).
Você acha que uma matriz parece lindo, se o único número um da matriz está localizado em seu meio (na célula que está na interseção da terceira linha e da terceira coluna). Conte o número mínimo de movimentos necessários para tornar a matriz bonita.

Entrada
A entrada consiste em cinco linhas, cada linha contém cinco inteiros: o jé o inteiro no eua linha da entrada representa o elemento da matriz que está localizado na interseção do eua primeira linha e a j- a coluna. É garantido que a matriz consiste em 24 zeros e um único número um.

Saída
Imprimir um único inteiro — o número mínimo de movimentos necessários para tornar a matriz bonita.

Exemplos
Entrada
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

Saída
3

-------------

Entrada
0 0 0 0 0
0 0 0 0 0
0 1 0 0 0
0 0 0 0 0
0 0 0 0 0

Saída
1
'''
i = 0

v1 = input().split()
v2 = input().split()
v3 = input().split()
v4 = input().split()
v5 = input().split()
matriz = [v1, v2, v3, v4, v5]

while(i < 5):
    for j in range(0, 5):
	    if(int(matriz[i][j]) == 1):
		    print(abs(2-i)+abs(2-j))
		    break
    i += 1