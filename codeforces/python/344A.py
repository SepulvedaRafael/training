'''
344A - ÍMÃS (MAGNETS)

O cientista louco Mike se diverte organizando fileiras de dominós. Ele não precisa de dominós, porém: ele usa ímãs retangulares em vez disso. Cada ímã tem dois pólos, positivo (um "mais") e negativo (um "menos"). Se dois ímãs são colocados juntos a uma distância próxima, então os pólos semelhantes se repelem e os pólos opostos se atraem.

Mike começa colocando um ímã horizontalmente sobre a mesa. Durante cada passo seguinte, Mike adiciona mais um ímã horizontalmente à extremidade direita da linha. Dependendo de como Mike coloca o ímã na mesa, ele é atraído pelo anterior (formando um grupo de vários ímãs ligados) ou repelido por ele (então Mike coloca esse ímã a alguma distância à direita do anterior). Assumimos que um único ímã não ligado a outros forma um grupo próprio.

  +--------------+-------+-----------+
  |	- + - + - +  |  - +  |  - + - +  |
  +--------------+-------+-----------+

Mike arranjou vários ímãs em uma fileira. Determine o número de grupos que os ímãs formaram.

Entrada
A primeira linha da entrada contém um inteiro n (1 ≤ n ≤ 100000) — o número de ímanes. Então n as linhas seguem. O eulinha -th (1 ≤ eu ≤ n) contém os caracteres "01", se o Mike pôs o euímã na posição "mais-menos", ou caracteres "10", se o Mike colocar o íman na posição "menos mais".

Saída
Na linha única da saída, imprima o número de grupos de ímãs.

Exemplos
Entrada
6
10
10
10
01
10
10

Saída
3

-----------

Entrada
4
01
01
10
10

Saída
2

Nota
O primeiro caso de teste corresponde à figura. O testcase tem três grupos que consistem em três, um e dois ímãs.

O segundo caso de teste tem dois grupos, cada um composto por dois ímãs.
'''
nGrupos = 0
i = 1
prox = ''

n = int(input())

if(n >= 1 and n <= 100000):
	while (i <= n):
		ima = input()

		if ima != prox:
			nGrupos += 1
			prox = ima

		i += 1

print(nGrupos)