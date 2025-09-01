'''
2161 - RAIZ QUADRADA DE 10

Uma das formas de calcular a raiz quadrada de um número natural é pelo método das frações periódicas continuadas. Esse método usa como denominador uma repetição de frações. Essa repetição pode ser feita uma quantidade específica de vezes.

Por exemplo, ao repetir 2 vezes a fração continuada para calcular a raiz quadrada de 10, temos a fórmula abaixo.

sqrt(10) aprox = 3 + 1 / (6 + (1 / 6))

Sua tarefa é, dado o número N de repetições, calcular o valor aproximado da raiz quadrada de 10.

Entrada
A entrada é um número natural N (0 ≤ N ≤ 100), que indica o número de repetições do denominador na fração continuada.

Saída
A saída é o valor aproximado da raiz quadrada com 10 casas decimais.

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  0                               |  3.0000000000                  |
+----------------------------------+--------------------------------+

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  1                               |  3.1666666667                  |
+----------------------------------+--------------------------------+

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  5                               |  3.1622776623                  |
+----------------------------------+--------------------------------+
'''
n = int(input())

x = 0.0
for i in range(n):
    x += 6.0
    x = (1.0 / x)
x += 3.0
print(f'{x:.10f}')