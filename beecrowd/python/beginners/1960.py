'''
1960 - NUMERAÇÃO ROMANA PARA NÚMREOS DE PÁGINA

A ECI (Editio Chronica Incredibilis ou Editora de Crônicas Incríveis) é muito tradicional quando se trata de numerar as páginas de seus livros. Ela sempre usa a numeração romana para isso. E seus livros nunca ultrapassam as 999 páginas pois, quando necessário, dividem o livro em volumes.

Voce deve escrever um programa que, dado um número arábico, mostra seu equivalente na numeração romana.

Lembre que I representa 1, V é 5, X é 10, L é 50, C é 100, D é 500 e M representa 1000.

Entrada
A entrada é um número inteiro positivo N (0 < N < 1000).

Saída
A saída é o número N escrito na numeração romana em uma única linha. Use sempre letras maiúsculas.

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  666                             |  DCLXVI                        |
+----------------------------------+--------------------------------+

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  83                              |  LXXXIII                       |
+----------------------------------+--------------------------------+

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  999                             |  CMXCIX                        |
+----------------------------------+--------------------------------+
'''
n = int(input())

symbols = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
}

while n != 0:
    if n >= symbols["M"]:
        print('M', end='')
        n -= symbols['M']
    elif n >= symbols['CM']:
        print('CM', end='')
        n -= symbols['CM']
    elif n >= symbols['D']:
        print('D', end='')
        n -= symbols['D']
    elif n >= symbols['CD']:
        print('CD', end='')
        n -= symbols['CD']
    elif n >= symbols['C']:
        print('C', end="")
        n -= symbols['C']
    elif n >= symbols['XC']:
        print('XC', end="")
        n -= symbols['XC']
    elif n >= symbols['L']:
        print('L', end="")
        n -= symbols['L']
    elif n >= symbols['XL']:
        print('XL', end="")
        n -= symbols['XL']
    elif n >= symbols['X']:
        print('X', end ="")
        n -= symbols['X']
    elif n >= symbols['IX']:
        print('IX', end="")
        n -= symbols['IX']
    elif n >= symbols['V']:
        print('V', end='')
        n -= symbols['V']
    elif n >= symbols['IV']:
        print('IV', end='')
        n -= symbols['IV']
    elif n >= symbols['I']:
        print('I', end='')
        n -= symbols['I']
print()