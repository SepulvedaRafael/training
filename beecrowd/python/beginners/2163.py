'''
2163 - O DESPERTAR DA FORÇA

Há muito tempo atrás, em uma galáxia muito, muito distante...

Após o declínio do Império, sucateiros estão espalhados por todo o universo procurando por um sabre de luz perdido. Todos sabem que um sabre de luz emite um padrão de ondas específico: 42 cercado por 7 em toda a volta. Você tem um sensor de ondas que varre um terreno com N x M células. Veja o exemplo abaixo para um terreno 4 x 7 com um sabre de luz nele (na posição (2, 4)).



Você deve escrever um programa que, dado um terreno N x M, procura pelo padrão do sabre de luz nele. Nenhuma varredura tem mais do que um padrão de sabre de luz.

Entrada
A primeira linha da entrada tem dois números positivos N e M, representando, respectivamente, o número de linhas e de colunas varridos no terreno (3 ≤ N, M ≤ 1000). Cada uma das próximas N linhas tem M inteiros, que descrevem os valores lidos em cada célula do terreno (-100 ≤ Tij ≤ 100, para 1 ≤ i ≤ N e 1 ≤ j ≤ M).

Saída
A saída é uma única linha com 2 inteiros X e Y separados por um espaço. Eles representam a coordenada (X,Y) do sabre de luz, caso encontrado. Se o terreno não tem um padrão de sabre de luz, X e Y são ambos zero.

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  4 7                             |  2 4                           |
|  11 12 7 7 7 13 14               |                                |
|  15 6 7 42 7 7 42                |                                |
|  98 -5 7 7 7 42 7                |                                |
|  -1 42 3 9 7 7 7                 |                                |
+----------------------------------+--------------------------------+

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  4 7                             |  0 0                           |
|  11 12 7 7 7 13 14               |                                |
|  15 6 7 12 7 7 42                |                                |
|  98 -5 7 7 7 42 7                |                                |
|  -1 42 3 9 7 7 7                 |                                |
+----------------------------------+--------------------------------+

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  3 3                             |  2 2                           |
|  7 7 7                           |                                |
|  7 42 7                          |                                |
|  7 7 7                           |                                |
+----------------------------------+--------------------------------+
'''
n, m = map(int, input().split())

l = []
r = []
a = 0
b = 0

for i in range(n):
    linha = input().split()
    for j in range(m):
        r.append(int(linha[i]))
    l.append(r)
    r = []

j = 0
for k in range(n):
    for o in range(m):
        if (l[k][o] == 42):
            try:
                if (l[k][o - 1] == 7 and l[k][o + 1] == 7 and l[k-1][o] == 7 and l[k-1][o - 1] == 7 and l[k-1][o+1] == 7 and l[k+1][o] == 7 and l[k+1][o-1] == 7 and l[k+1][o+1] == 7):
                    print('DEU')
                    a = k+1
                    b = i+1
                    j = 1
            except IndexError:
                pass
if j == 1:
    print(a, b)

if j == 0:
    print("0 0")