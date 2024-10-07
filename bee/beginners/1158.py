'''
1158 - SOMA DE ÍMPARES CONSECUTIVOS III

Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de Y ímpares consecutivos a partir de X inclusive o próprio X se ele for ímpar. Por exemplo:
para a entrada 4 5, a saída deve ser 45, que é equivalente à: 5 + 7 + 9 + 11 + 13
para a entrada 7 4, a saída deve ser 40, que é equivalente à: 7 + 9 + 11 + 13

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma dos consecutivos números ímpares a partir do valor X.

+------------------------+--------------------------------+
|   Exemplo de Entrada   |       Exemplo de Saída         |
+------------------------+--------------------------------+
|           2            |               21               |
|          4 3           |               24               |
|         11 2           |                                |
+------------------------+--------------------------------+
'''
i = 1
n = int(input())

while(i <= n):
    x, y = map(int, input().split())
    output = 0

    for j in range(0, y + 1):
        if(j == y):
            print(output)
            break
        else:
            if((x % 2) == 0):
                x += 1
                output += x
                x += 2
            else:
                output += x
                x += 2
    i += 1