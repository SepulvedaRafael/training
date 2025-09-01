'''
1827 - MATRIZ QUADRADA IV

Neste programa seu trabalho é ler um valor inteiro que será o tamanho da matriz quadrada (largura e altura) que será preenchida da seguinte forma: a parte externa é preenchida com 0, a parte interna é preenchida com 1, a diagonal principal é preenchida com 2, a diagonal secundária é preenchida com 3 e o ponto central contém o valor 4, conforme os exemplos abaixo.

Obs: o quadrado com '1' sempre começa na posição tamanho/3, tanto na largura quanto quanto na altura. A linha e a coluna começam em zero (0).

Entrada
A entrada contém vários casos de teste e termina com EOF (fim de arquivo. Cada caso de teste consiste de um valor inteiro ímpar N (5 ≤ N ≤ 101) que é o tamanho da matriz.

Saída
Para cada caso de teste, imprima a matriz correspondente conforme o exemplo abaixo. Após cada caso de teste, imprima uma linha em branco.

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  2                               |  20003                         |
|  11                              |  01110                         |
|                                  |  01410                         |
|                                  |  01110                         |
|                                  |  30002                         |
|                                  |                                |
|                                  |  20000000003                   |
|                                  |  02000000030                   |
|                                  |  00200000300                   |
|                                  |  00011111000                   |
|                                  |  00011111000                   |
|                                  |  00011111000                   |
|                                  |  00011111000                   |
|                                  |  00011111000                   |
+----------------------------------+--------------------------------+
'''

while True:
    try:
        n = int(input())
        s = int(n/3)
        e = n-s

        # FILL WITH 0
        m = [[0 for i in range(n)] for j in range(n)]

        # FILL WITH 2
        for i in range(n):
            m[i][i] = 2

        # FILL WITH 3
        j = 0
        for i in range(n-1,-1,-1):
            m[j][i] = 3
            j += 1

        # FILL MIDDLE WITH 1
        for i in range(s, e):
            for j in range(s, e):
                m[i][j] = 1

        m[int(n/2)][int(n/2)] = 4

        for i in range(n):
            for j in range(n):
                print(m[j][i], end='')
            print()
        print()

    except EOFError:
        break