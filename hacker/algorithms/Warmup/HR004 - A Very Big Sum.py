'''
HR004 - A Very Big Sum
Neste desafio, você é obrigado a calcular e imprimir a soma dos elementos em uma matriz, tendo em mente que alguns desses inteiros podem ser bastante grandes.

Descrição da Função
Completar o aVeryBigSum função no editor abaixo. Ele deve retornar a soma de todos os elementos da matriz.

aVeryBigSum tem o seguinte parâmetro(s):
int ar[n]: uma matriz de inteiros .

Retorno
longo: a soma de todos os elementos da matriz

Formato de Entrada
A primeira linha da entrada consiste em um inteiro .
A próxima linha contém inteiros separados por espaço contidos na matriz.

Formato de Saída
Retorna a soma inteira dos elementos na matriz.

Restrições
1 <= n <= 10
0 <= ar[i] <= 10**10

Entrada de Amostra
5
1000000001 1000000002 1000000003 1000000004 1000000005

Saída
5000000015

Nota:
O intervalo do número inteiro de 32 bits é.
(-2**31) to (2**31 - 1) or [-2147483648, 2147483647]

Quando adicionamos vários valores inteiros, a soma resultante pode exceder o intervalo acima. Talvez seja necessário usar long int C/C++/Java para armazenar essas somas.
'''
def aVeryBigSum(ar):
    soma = 0
    for i in ar:
        soma += i
    return print(soma)

ar_count = int(input().strip())
ar = list(map(int, input().rstrip().split()))
result = aVeryBigSum(ar)