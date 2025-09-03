'''
136A - PRESENTES (PRESENTS)

O pequeno Petya gosta muito de presentes. Recentemente, ele recebeu um novo laptop como um presente de Ano Novo de sua mãe. Ele imediatamente decidiu dar a outra pessoa como o que pode ser mais agradável do que dar presentes a alguém. E nesta ocasião ele organizou uma festa de Ano Novo em sua casa e convidou n seus amigos lá.

Se há uma coisa que Petya gosta mais do que receber presentes, é ver os outros dando presentes para outra pessoa. Assim, ele escondeu o laptop com segurança até o próximo Ano Novo e decidiu assistir seus amigos trocando presentes enquanto ele não participa do processo. Ele numerava todos os seus amigos com números inteiros de 1 para n. Petya lembrou que um número de amigo eu deu um presente para um número de amigo peu. Ele também lembrou que cada um de seus amigos recebeu exatamente um presente.

Agora Petya quer saber para cada amigo eu o número de um amigo que lhe deu um presente.

Entrada
A primeira linha contém um inteiro n (1 ≤ n ≤ 100— a quantidade de amigos que Petya convidou para a festa. A segunda linha contém n inteiros separados por espaço: o euo número é peu — o número de um amigo que deu um presente ao número de amigo eu. É garantido que cada amigo recebeu exatamente um presente. É possível que alguns amigos não compartilhem as idéias de Petya de dar presentes a outra pessoa. Esses amigos deram os presentes para si mesmos.

Saída
Imprimir n inteiros separados por espaço: o euo número deve ser igual ao número do amigo que deu um presente ao número do amigo eu.

Exemplos
Entrada
4
2 3 4 1

Saída
4 1 2 3

-------------

Entrada
3
1 3 2

Saída
1 3 2

---------------

Entrada
2
1 2

Saída
1 2
'''
n = int(input())
p = map(int, input().split())
positions = {}

for i, valor in enumerate(p):
	positions[valor] = i + 1

for j in range(n):
	print(positions[j + 1], end=" ")