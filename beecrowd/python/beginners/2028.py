'''
2028 - SEQUÊNCIA DE SEQUÊNCIA

Hyam é um menino que adora sequências. Ele anda descobrindo sequências interessantes que nem mesmo Fibonacci imaginaria. Certo dia, Hyam percebeuque dado um número N, ele poderia fazer uma sequência do tipo 0 1 2 2 3 3 3 4 4 4 4 ... N N N ... N. No entanto, Hyam percebeu que cada valor que aumentava no número da sequência, a quantidade total de números da sequência aumentava semelhantemente à um crescimento fatorial, neste caso, ao invés de multiplicar, soma-se o número total de números da sequência com o valor do próximon úmero da sequência. Por exemplo, se N = 2. A sequência correta seria 0 1 2 2, obtendo-se 4 digitos. Agora, se N = 3, o próximo número da sequência tem valor 3, então a quantidade total de número da sequência seria a quantidade de números com N = 2, que é 4, mais o valor do próximo número da sequência, neste caso, obtendo-se 7, já que a sequência correta para N = 3 é 0 1 2 2 3 3 3.

Sua tarefa é fazer um algoritmo que dado um número inteiro N, tenha como resposta a quantidade total de números dessa sequência e logo abaixo a sequência completa.

Entrada
A entrada é composta de vários casos de testes. Cada caso é composto por um inteiro N (0 <= N <= 200) que indica o valor dos últimos N números da sequência.

A entrada termina com final de arquivo (EOF).

Saída
A saída é no formato Caso X: N numeros onde X é a ordem do número de casos e N é a quantidade de números que contpem na sequência completa, na próxima linha a sequência dos números com um espaço entre eles. É pedido que deixe uma linha em branco após cada caso.

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  0                               |  Caso 1: 1 numero              |
|  1                               |  0                             |
|  2                               |                                |
|  3                               |  Caso 2: 2 numeros             |
|                                  |  0 1                           |
|                                  |                                |
|                                  |  Caso 3: 4 numeros             |
|                                  |  0 1 2 2                       |
|                                  |                                |
|                                  |  Caso 4: 7 numeros             |
|                                  |  0 1 2 2 3 3 3                 |
|                                  |                                |
+----------------------------------+--------------------------------+
'''
def sequence(num):
    nums = []
    for i in range(n + 1):
        if i == 0:
            nums.append(0)

        for k in range(i):
            nums.append(i)
    return [len(nums), nums]

case = 1
while True:
    try:
        n = int(input())

        if n == 0:
            print(f'Caso {case}: {sequence(n)[0]} numero')
            print(*sequence(n)[1], sep=" ")
        else:
            print(f'Caso {case}: {sequence(n)[0]} numeros')
            print(*sequence(n)[1], sep=" ")
        print()
        case += 1
    except EOFError:
        break