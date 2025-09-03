'''
HR002 - Simples Array Sum
Dada uma matriz de inteiros, encontre a soma de seus elementos.

Por exemplo, se a matriz ar = [1, 2, 3] 1 + 2 + 3 = 6, então volte 6.

Descrição da Função
Completar o simpleArraySum função no editor abaixo. Ele deve retornar a soma dos elementos da matriz como um inteiro.

simpleArraySum tem o seguinte parâmetro(s):
ar: uma matriz de inteiros

Formato de Entrada
A primeira linha contém um número inteiro , denotando o tamanho da matriz.
A segunda linha contém inteiros separados por espaço que representam os elementos da matriz.

Restrições
0 < n, ar[i] <= 1000

Formato de Saída
Imprima a soma dos elementos da matriz como um único inteiro.

Entrada de Amostra
6
1 2 3 4 10 11

Saída da Amostra
31

Explicação
Nós imprimimos a soma dos elementos da matriz:
1 + 2 + 3 + 4 + 10 + 11 = 31
'''
def simpleArraySum(ar):
    sum = 0
    for i in ar:
        sum += i
    return sum

ar_count = int(input().strip())
ar = list(map(int, input().rstrip().split()))
result = simpleArraySum(ar)
print(result)