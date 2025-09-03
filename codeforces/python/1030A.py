'''
1030A - EM BUSCA DE UM PROBLEMA FÁCIL (IN SEARCH OF AN EASY PROBLEM)

Ao preparar um torneio, os coordenadores da Codeforces tentam fazer o melhor para tornar o primeiro problema o mais fácil possível. Desta vez, o coordenador tinha escolhido algum problema e perguntou n
pessoas sobre suas opiniões. Cada pessoa respondeu se esse problema é fácil ou difícil.

Se pelo menos um deles n
as pessoas responderam que o problema é difícil, o coordenador decide mudar o problema. Para as respostas dadas, verifique se o problema é fácil o suficiente.

Entrada
A primeira linha contém um único número inteiro n
(1≤n≤100
— número de pessoas que foram convidadas a dar as suas opiniões.

A segunda linha contém n
inteiros, cada inteiro é 0
ou 1
. Se eu
o inteiro é 0
, então eu
a pessoa pensa que o problema é fácil; se é 1
, então eu
a pessoa pensa que o problema é difícil.

Saída
Imprimir uma palavra: "FÁCIL"se o problema é fácil de acordo com todas as respostas, ou "DIFÍCIL"se há pelo menos uma pessoa que acha que o problema é difícil.

Você pode imprimir todas as cartas em qualquer registro: "FÁCIL", "fácil", "EASY"e "eaSY"todos serão processados corretamente.

Exemplos
Entrada
3
0 0 1

Saída
HARD

-----------
Entrada
1
0

Saída
EASY

Nota
No primeiro exemplo, a terceira pessoa diz que é um problema difícil, por isso deve ser substituído.

No segundo exemplo, o problema é fácil para a única pessoa, por isso não precisa ser substituído.
'''
n = int(input())
peoples = list(map(int, input().split()))

if(n >= 1 and n <=  100):
	if(1 in peoples):
		print('HARD')
	else:
		print('EASY')