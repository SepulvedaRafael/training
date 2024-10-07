'''
677A - VANYA E CERCA (VANYA AND FENCE)

Vanya e seus amigos estão andando ao longo da cerca de altura h e eles não querem que o guarda os observe. Para conseguir isso, a altura de cada um dos amigos não deve exceder h. Se a altura de uma pessoa é maior do que h ele pode se curvar e então ele certamente não será notado pelo guarda. A altura do eua pessoa é igual a aeu.

Considere a largura da pessoa andando como de costume para ser igual a 1, enquanto a largura da pessoa dobrada é igual a 2. Os amigos querem falar uns com os outros enquanto caminham, então eles gostariam de andar em uma única linha. Qual é a largura mínima da estrada, de modo que os amigos podem andar em uma fileira e permanecer sem vigilância do guarda?

Entrada
A primeira linha da entrada contém dois inteiros n e h (1 ≤ n ≤ 1000 1 ≤ h ≤ 1000— o número de amigos e a altura da cerca, respetivamente.

A segunda linha contém n inteiros aeu (1 ≤ aeu ≤ 2h), o euum deles é igual à altura do eu- a pessoa.

Saída
Imprimir um único inteiro — a largura mínima possível válida da estrada.

Exemplos
Entrada
3 7
4 5 14

Saída
4

---------------
Entrada
6 1
1 1 1 1 1 1

Saída
6
---------------
Entrada
6 5
7 6 8 9 10 5

Saída
11

Nota
Na primeira amostra, apenas o número de pessoa 3 deve dobrar para baixo, de modo que a largura necessária é igual a 1 + 1 + 2 = 4.

Na segunda amostra, todos os amigos são curtos o suficiente e ninguém tem que dobrar, então a largura 1 + 1 + 1 + 1 + 1 + é suficiente.

Na terceira amostra, todas as pessoas têm que se dobrar, exceto a última. A largura mínima exigida da estrada é igual a 2 + 2 + 2 + 2 + 2 + 1 = 11.
'''
larMin = 0

n, h = map(int, input().split())

a = list(input().split())

for i in a:
	if(int(i) > h):
		larMin += 2
	else:
		larMin += 1

print(larMin)