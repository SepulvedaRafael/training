'''
200B - Bebidas (Drinks)

O pequeno Vasya ama muito suco de laranja. É por isso que qualquer comida e bebida em sua cozinha necessariamente contém suco de laranja. Há n bebidas em sua geladeira, a fração de volume de suco de laranja na i -ésima bebida é igual a p i por cento.

Um dia, Vasya decidiu fazer um coquetel de laranja para si. Ele pegou proporções iguais de cada uma das n bebidas e as misturou. Então ele se perguntou quanto suco de laranja o coquetel tinha.

Encontre a fração de volume do suco de laranja na bebida final.

Entrada
A primeira linha de entrada contém um único inteiro n ( 1 ≤  n  ≤ 100 ) — o número de bebidas contendo laranja na geladeira de Vasya. A segunda linha contém n inteiros p i ( 0 ≤  p i  ≤ 100 ) — a fração de volume de suco de laranja na i -ésima bebida, em porcentagem. Os números são separados por um espaço.

Saída
Imprima a fração de volume em porcentagem de suco de laranja no coquetel de Vasya. A resposta será considerada correta se o erro absoluto ou relativo não exceder 10   - 4 .

Exemplos
Entrada
3
50 50 100

Saída
66.666666666667

-----------------

Entrada
4
0 25 50 75

Saída
37.500000000000

Oservação
Nota para a primeira amostra: vamos supor que Vasya pegue x mililitros de cada bebida da geladeira. Então o volume de suco puro no coquetel será igual a mililitros. O volume total do coquetel é igual a 3· x mililitros, então a fração de volume do suco no coquetel é igual a , ou seja, 66,(6) por cento
'''
volumeSuco = 0
n = int(input())
p = list(map(int, input().rstrip().split()))

for i in p:
	volumeSuco += i

volumeSuco /= n

print(f'{volumeSuco:.12f}')