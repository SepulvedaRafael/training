'''
2159 - NÚMERO APROXIMADO DE PRIMOS

Schoenfeld e Rosser publicaram em 1962 um artigo descrevendo um valor mínimo e máximo para a quantidade de números primos até n, para n ≥ 17. Esta quantidade é representada pela função (n) e a fórmula é mostrada abaixo.

n / ln(n) < (n) < 1.25506 * n / ln(n)

Sua tarefa é, dado um natural n, calcular o mínimo e máximo do intervalo para o número aproximado de primos até n.

Entrada
A entrada é um número natural n (17 ≤ n ≤ 109).

Saída
A saída são dois valores P e M com 1 casa decimal cada, tal que P < (n) < M, de acordo com a fórmula dada acima. Os valores devem ser separados por um espaço em branco.

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  17                              |  6.0 7.5                       |
+----------------------------------+--------------------------------+

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  50                              |  12.8 16.0                     |
+----------------------------------+--------------------------------+

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  100                             |  21.7 27.3                     |
+----------------------------------+--------------------------------+
'''
import math

n = int(input())

print(f'{(n / math.log(n)):.1f} {1.25506 * (n / math.log(n)):.1f}')