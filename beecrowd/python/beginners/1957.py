'''
1957 - CONVERTER PARA HEXADECIMAL

Os dados armazenados no computador estão em binário. Uma forma econômicade ver estes números é usar a base 16 (hexadecimal).

Sua tarefa consiste em escrever um programa que, dado um número natural na base 10, mostre sua representação em hexadecimal.

Entrada
A entrada é um número inteiro positivo V na base 10 (1 <= V <= 2 x 10^9)

Sída
A saída é o mesmo número V na base 16 em uma única linha (não esqueça do caractere de fim-de-linha). Use letras maiúsculas, conforme os exemplos.

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  10                              |  A                             |
+----------------------------------+--------------------------------+

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  15                              |  F                             |
+----------------------------------+--------------------------------+

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  16                              |  10                            |
+----------------------------------+--------------------------------+

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  31                              |  1F                            |
+----------------------------------+--------------------------------+

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  65535                           |  FFFF                          |
+----------------------------------+--------------------------------+
'''
v = int(input())

print(hex(v)[2:].upper())