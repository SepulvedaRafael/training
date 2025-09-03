'''
HR014 - Between Two Sets
Haverá duas matrizes de inteiros. Determine todos os números inteiros que satisfaçam as duas condições seguintes:

1. Os elementos da primeira matriz são todos os fatores do número inteiro sendo considerados
2. O número inteiro sendo considerado é um fator de todos os elementos da segunda matriz

Esses números são chamados de ser entre as duas matrizes. Determine quantos desses números existem.

Exemplo
a = [2, 6]
b = [24, 36]

Há dois números entre as matrizes: 6 e 12.
6 % 2 = 0 6 % 6 = 0 24 % 6 = 0 36 % 6 = 0 para o primeiro valor.
12 % 2 = 0 12 % 6 = 0 24 % 12 = 0 36 % 12 = 0 para o segundo valor.
Retorno 2.

Descrição da Função
Completar o getTotalX função no editor abaixo. Ele deve retornar o número de inteiros que são betwen os conjuntos.

getTotalX tem o seguinte parâmetro(s):
a[n]: uma matriz de inteiros
b[m]: uma matriz de inteiros

Retorna
int: o número de inteiros que estão entre os conjuntos

Formato de Entrada
A primeira linha contém dois números inteiros separados por espaço e , o número de elementos em matrizes n e m.
A segunda linha contém inteiros separados por espaço distintos a[i] onde 0 <= i < n.
A terceira linha contém inteiros separados por espaço distintos b[j] onde 0 <= j < m.

Restrições
1 <= n, m <= 10
1 <= a[i] <= 100
1 <= b[j] <= 100

Entrada de Amostra
2 3
2 4
16 32 96

Saída da Amostra
3

Explicação
2 E 4 dividem-se uniformemente em 4, 8, 12 e 16.
4, 8 e 16 dividem-se uniformemente em 16, 32, 96.
4, 8 e 16 são os únicos três números para os quais cada elemento de a é um fator e cada um é um fator de todos os elementos de b.
'''
n, m = map(int, input().rstrip().split())
arr = list(map(int , input().rstrip().split()))
brr = list(map(int , input().rstrip().split()))