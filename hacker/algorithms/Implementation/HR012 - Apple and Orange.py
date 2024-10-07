'''
HR012 - Apple and Orange
A casa de Sam tem uma macieira e uma laranjeira que produzem uma abundância de frutas. Usando as informações dadas abaixo, determine o número de maçãs e laranjas que pousam na casa de Sam.

No diagrama abaixo:
- A região vermelha denota a casa, onde s é o ponto de partida, e t é o ponto final. A macieira está à esquerda da casa e a laranjeira à sua direita.
- Suponha que as árvores estejam localizadas em um único ponto, onde a macieira esteja no ponto a e a laranjeira está no ponto b.
- Quando um fruto cai de sua árvore, ele cai d unidades de distância de sua árvore de origem ao longo do x- eixo. *Um valor negativo de d significa que a fruta caiu d unidades à esquerda da árvore, e um valor positivo de d significa que cai unidades à direita da árvore. *

Dado o valor de d para m maçãs e n laranjas, determine quantas maçãs e laranjas cairão na casa de Sam (ou seja, na faixa inclusiva [s, t])?

Por exemplo, a casa do Sam está entre s = 7 e t = 10. A macieira está localizada em a = 4 e a laranja em b = 12. Existem m = 3 maçãs e n = 3 laranjas. Maçãs são jogadas apples = [2, 3, -4] unidades distância de a, e oranges = [3, -2, -4] unidades distância. Adicionando cada distância da maçã à posição da árvore, eles pousam em [4 + 2, 4 + 3, 4 + -4] = [6, 7, 0]. Laranjas pousam em [12 + 3, 12 + -2, 12 + -4] = [15, 10, 8]. Uma maçã e duas laranjas pousam na faixa inclusiva 7 - 10 então nós imprimimos:
		1
		2

Descrição da Função
Completar o countApplesAndOranges função no editor abaixo. Deve imprimir o número de maçãs e laranjas que pousam na casa de Sam, cada uma em uma linha separada.

countApplesAndOranges tem o seguinte parâmetro(s):
s: inteiro, ponto de partida da localização da casa de Sam.
t: inteiro, localização final da localização da casa de Sam.
a: inteiro, localização da árvore da Apple.
b: inteiro, localização da árvore laranja.
maçãs: matriz inteira, distâncias em que cada maçã cai da árvore.
laranjas: matriz inteira, distâncias em que cada laranja cai da árvore.

Formato de Entrada
A primeira linha contém dois inteiros separados por espaço, denotando os respectivos valores de s e t.
A segunda linha contém dois inteiros separados por espaço, denotando os respectivos valores de a e b.
A terceira linha contém dois inteiros separados por espaço, denotando os respectivos valores de m e n.
A quarta linha contém m inteiros separados por espaço denotando as respectivas distâncias que cada maçã cai do ponto a.
A quinta linha contém n inteiros separados por espaço denotando as respectivas distâncias que cada laranja cai do ponto b.

Restrições
1 <= s, t, a, b, m, n >= 10**5
-10**5 <= d <= 10**5
a < s < t < b


Formato de Saída
Imprimir dois inteiros em duas linhas diferentes:
1. O primeiro número inteiro: o número de maçãs que caem na casa de Sam.
2. O segundo número inteiro: o número de laranjas que caem na casa de Sam.

Entrada da amostra 0
711
5 15
3 2
2 2 1
5 -6

Saída da amostra 0
1
1

Explicação 0
A primeira maçã cai na posição 5 - 2 = 3.
A segunda maçã cai na posição 5 + 2 = 7.
A terceira maçã cai na posição 5 + 1 = 6.
A primeira laranja cai na posição 15 + 5 = 20.
A segunda laranja cai na posição 15 - 6 = 9.
Apenas uma fruta (a segunda maçã) cai dentro da região entre 7 e 11, então nós imprimimos 1 como nossa primeira linha de saída.
Apenas a segunda laranja cai dentro da região entre 7 e 11, então nós imprimimos 1 como nossa segunda linha de saída.
'''
s, t = map(int, input().rstrip().split()) # Ponto de partida e ponto final
a, b = map(int, input().rstrip().split()) # Localização da árvore Apple e Orange
m, n = map(int, input().rstrip().split()) # Quantidade de maçãs e laranjas
apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))

inIntervalApple = 0
inIntervalOrange = 0

# Maçãs
for i in apples:
	calc = a + i

	if(calc >= s and calc <= t):
		inIntervalApple += 1

# Laranjas
for j in oranges:
	calc = b + j

	if(calc >= s and calc <= t):
		inIntervalOrange += 1

print(inIntervalApple)
print(inIntervalOrange)