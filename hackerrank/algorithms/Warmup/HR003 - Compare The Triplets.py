'''
HR0003 - Compare The Triplets
Alice e Bob criaram um problema para o HackerRank. Um revisor classifica os dois desafios, atribuindo pontos em uma escala de 1 para 100 para três categorias: clareza do problema originalidade, e dificuldade.

A classificação para o desafio de Alice é o trigêmeo a = (a[0], a[1], a[2]), e a classificação para o desafio de Bob é o trigêmeo b = (b[0], b[1], b[2]).

A tarefa é encontrar o seu pontos de comparação comparando a[0] com b[0] a[1] com b[1], e a[2] com b[2].

Se a[i] > b[i], então Alice é premiada 1 ponto.
Se a[i] < b[i], então Bob é premiado 1 ponto.
Se a[i] = b[i]nenhuma das pessoas recebe um ponto.
Pontos de comparação são o total de pontos que uma pessoa ganha.

Dado a e b, determinar seus respectivos pontos de comparação.

Exemplo
a = [1, 2, 3]
b = [3, 2, 1]

Para os elementos *0*, Bob recebe um ponto porque a[0] .
Para os elementos iguais a[1] e b[1], nenhum ponto é ganho.
Finalmente, para os elementos 2 a[2] > b[2] então Alice recebe um ponto.
A matriz de retorno é [1, 1] com a pontuação de Alice em primeiro lugar e a de Bob em segundo.

Descrição da Função
Complete a função compararTriplets no editor abaixo.

compareTriplets tem o seguinte parâmetro(s):
a[3]: Classificação de desafio de Alice
b[3]: Classificação de desafio de Bob

Retorno
int[2]: A pontuação de Alice está na primeira posição, e a pontuação de Bob está na segunda.

Formato de Entrada
A primeira linha contém 3 inteiros separados por espaço, a[0] a[1], e a[2], os respectivos valores em tripleto a.
A segunda linha contém 3 inteiros separados por espaço, b[0] b[1], e b[2], os respectivos valores em tripleto b.

Restrições
1 ≤ a[i] ≤ 100
1 ≤ b[i] ≤ 100

Entrada da amostra 0
5 6 7
3 6 10

Saída
11

Explicação 0
Neste exemplo:
- a = (a[0], a[1], a[2]) = (5, 6, 7)
- b = (b[0], b[1], b[2]) = (3, 6, 10)

Agora, vamos comparar cada pontuação individual:
a[0] > b[0] é assim que Alice recebe ponto.
a[1] = b[1] então ninguém recebe um ponto.
a[2] < b[2] é assim que o Bob recebe ponto.

A pontuação de comparação de Alice é 1, e a pontuação de comparação de Bob é 1. Assim, retornamos a matriz [1, 1].

Entrada da amostra 1
17 28 30
99 16 8

Saída da amostra 1
21

Explicação 1
Comparando o 0th elementos, 17 < 99 então Bob recebe um ponto.
Comparando o 1th e 2th elementos, 28 > 16 e 30 > 8 então Alice recebe dois pontos.
A matriz de retorno é [2, 1].
'''
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

al = 0
bob = 0
for i in range(0, len(a)):
    if(a[i] > b[i]):
	    al += 1

    elif(a[i] == b[i]):
        al += 0
        bob += 0

    elif(a[i] < b[i]):
        bob += 1

print(al, bob)