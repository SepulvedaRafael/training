'''
HR005 - Diagonal Difference
Dada uma matriz quadrada, calcule a diferença absoluta entre as somas de suas diagonais.

Por exemplo, a matriz quadrada é mostrado abaixo:
1 2 3
4 5 6
9 8 9
A diagonal da esquerda para a direita = 1 + 5 + 9 = 15. A diagonal direita para esquerda = 3 + 5 + 9 = 17. A diferença absoluta é |15 - 17| = 2.

Descrição da função
Completar o diagonalDIfference função no editor abaixo.

diagonalDifference leva o seguinte parâmetro:
int arr[n][m]: uma matriz de inteiros

Retorno
int: a diferença diagonal absoluta

Formato de Entrada
A primeira linha contém um único número inteiro , o número de linhas e colunas na matriz quadrada .
Cada um dos próximos linhas descreve uma linha, , e consiste em inteiros separados por espaço .

Restrições
-100 <= arr[i][j] <= 100

Formato de Saída
Retorne a diferença absoluta entre as somas das duas diagonais da matriz como um único número inteiro.

Entrada de Amostra
3
11 2 4
4 5 6
10 8 -12

Saída
15

Explicação
A diagonal principal é:
11
   5
     -12
Soma na diagonal primária: 11 + 5 - 12 = 4

A diagonal secundária é:
     4
   5
10
Soma na diagonal secundária: 4 + 5 + 10 = 19
Diferença: |4 - 19| = 15

Nota: |x| é o valor absoluto de x
'''
n = int(input().strip())
arr = []

for _ in range(n):
  arr.append(list(map(int, input().rstrip().split())))

# Diagonal Principal
somaDP = 0
somaDS = 0
for i in range(n):
  for j in range(n):
    if(i == j):
      somaDP += arr[i][j]

# Diagonal Secundária
l = -1
for k in range(n):
  somaDS += arr[k][l]
  l -= 1

print(abs(somaDP - somaDS))