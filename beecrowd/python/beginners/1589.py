'''
1589 - BOB CONDUITE

Você tem em mãos dois cabos circulares de energia. O primeiro cabo tem raio R1 e o segundo raio R2. Você precisa comprar um conduite circular (veja a imagem abaixo que ilustra um conduite) de maneira a passar os dois cabos por dentro dele:

Qual o menor raio do conduite que você pode comprar? Em outras palavras, dado dois círculos, qual o raio do menor círculo que possa englobar ambos os dois?

Entrada
Na primeira linha teremos um inteiro T (T <= 10000), indicando o número de casos de teste.

Na única linha de cada caso teremos dois números inteiro R1 e R2, indicando os respectivos raios. Os inteiros serão positivos e todas ascontas caberão em um inteiro normal de 32 bits.

Saída
Em cada caso, imprima o menor raio possível em uma única linha.

+------------------------+--------------------------------+
|   Exemplo de Entrada   |       Exemplo de Saída         |
+------------------------+--------------------------------+
|           3            |  2                             |
|          1 1           |  10                            |
|          2 8           |  10                            |
|          8 2           |                                |
+------------------------+--------------------------------+
'''
t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    print(a + b)