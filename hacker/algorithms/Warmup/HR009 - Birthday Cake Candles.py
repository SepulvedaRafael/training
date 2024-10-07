'''
HR009 - Birthday Cake Candles
Você é responsável pelo bolo para o aniversário de uma criança. Você decidiu que o bolo terá uma vela para cada ano de sua idade total. Eles só serão capazes de soprar a mais alta das velas. Conte quantas velas são mais altas.

Exemplo
candles = [4, 4, 1, 3]

As velas de altura máxima são 4 unidades altas. Existem 2 deles, então volte 2.

Descrição da Função
Complete a função birthdayCakeCandles no editor abaixo.

birthdayCakeCandles tem o seguinte parâmetro(s):
int velas[n]: as alturas da vela

Retorna
int: o número de velas que são mais altas

Formato de Entrada
A primeira linha contém um único número inteiro é o tamanho de candles[].
A segunda linha contém números inteiros separados por espaço, onde cada número inteiro descreve a altura de candles[i].

Restrições
1 <= n <= 10**5
1 <= candles[i] <= 10**7

Entrada da amostra 0
4
3 2 1 3

Saída da amostra 0
2

Explicação 0
As alturas das velas são [3, 2, 1, 3]. As velas mais altas são 3 unidades, e há 2 deles.
'''
candles_count = int(input().strip())
velas = list(map(int, input().rstrip().split()))
cont = velas.count(max(velas))

print(cont)