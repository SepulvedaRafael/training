'''
1789 - A CORRIDA DE LESMAS

A corrida de lesmas é um esporte que cresceu muito nos últimos anos, fazendo com que vária pessoas dediquem suas vidas tentando capturar lesmas velozes, e treina-las para faturar mihlões em corridas pelo mundo. Porém a tarefa de capturar lesmas velozes não é uma tarefa muito fácil, pois particamente todas as lesmas são muito lentas. Cada lesma é classificada em um nível dependendo de sua velocidade:

Nível 1: Se a velocidade é menorque 10cm/h.
Nível 2:Se a velocidade é maior ou igual a 10cm/h e menor que 20cm/h.
Nível 3: Se a velocidade é mairo ou igual a 20cm/h.

Sua tarefa é identificar qual nível de velocidade da lesma mais veloz de um grupo de lesmas.

Entrada
A entrada consiste de múltiplos casos de teste, e cada um consiste em duas linhas: A primeira linha contém um inteiro L (1 <= L <= 500) representando o número de lesmas do grupo, e a segunda linha contém L inteiros Vi (1 <= Vi <= 50) representando as velocidade de cada lesma do grupo.

A entrada termina com o fim do arquivo (EOF).

Saída
Para cada caso de teste, imprima uma única linha indicando o nível de velocidade da lesma mais veloz do grupo.

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  10                              |  3                             |
|  10 10 10 10 15 18 20 15 11 10   |  1                             |
|  10                              |  2                             |
|  1 5 2 9 5 5 8 4 4 3             |                                |
|  10                              |                                |
|  19 9 1 4 5 8 6 11 9 7           |                                |
+----------------------------------+--------------------------------+
'''
while True:
    try:
        l = int(input())
        velocidade_lesma = max(list(map( int, input().split())))

        print(3 if velocidade_lesma >= 20 else 2 if velocidade_lesma >= 10 else 1)
    except EOFError:
        break