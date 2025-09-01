'''
1973 - JORNADA NAS ESTRELAS

Após comprar vários sítios adjacentes na região do oeste catarinense, a família Estrela construiu uma única estrada que passa por todos os sítios em sequência. O primeirio sítio da sequência foi batizado de Estrela 1, o segundo de Estrela 2, e assim por diante. Porém, o irmão que vive em Estrela 1 acabou enlouquecendo e resolveu fazer uma Jornada nas Estrelas para roubar carneiros das propriedades de seus irmãos. Mas ele está definitivamente pirado. Quando passa pelo sítio Estrela i, ele rouba apenas um carnero daquele sítio (se o sítio tem algum) e segue ou para Estrela i + 1 ou para Estrela i - 1, dependendo se o número de carneiros em Estrela i era, respectivamente, ímpar ou par. Se não existe a Estrela para a qual ele deseja seguir, ele interrompe sua jornada. O irmão louco começa sua Jornada em Estrela 1, roubando um carneiro do seu próprio sítio.

Entrada
A primeira linha da entrada consiste de um único inteiro N (1 <= N <= 10^6), o qual representa o número de Estrelas. A segunda linha da entrada consiste de N inteiros, de modo que o i-ésimo inteiro Xi (1 <= Xi <= 10^6), representa o número inicial de carneiros em Estrela i.

Saída
Imprima uma linha contendo dois inteiros, de modo que o primeiro represente o número de EStrelas atacadas pelo irmão louco e o segundo represente o número total de carneiros não roubados.

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  8                               |  8 68                          |
|  1 3 5 7 11 13 17 19             |                                |
+----------------------------------+--------------------------------+

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  8                               |  7 63                          |
|  1 3 5 7 11 13 16 19             |                                |
+----------------------------------+--------------------------------+
'''
n = int(input())

l = list(map(int, input().split()))
temp = res = i = 0

while i < n and (l[i] % 2 != 0):
    if l[i] >= 1:
        l[i] = l[i] - 1
    i += 1
    temp = i

if temp != n:
    temp = temp + 1
    for e in reversed(range(temp)):
        if l[e] >= 1:
            l[e] = l[e] - 1

for w in range(n):
    res = res + l[w]

print(temp, res)