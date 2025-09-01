'''
1962 - HÁ MUITO, MUITO TEMPO ATRÁS

Raul Seixas cantava que nasceu há 10 mil anos atrás e não tinha nada nesse mundo que ele não sabia demais. Os Mamonas Assassinas cantavam que mais de 10 mil anos "se passaram-se" [sic] quando eles repetiram a 5a série. Tantos eventos passados e o professor MC ficou curioso para saber em que ano tudo isso aconteceu.

VocÊ deve escrever um programa que, dada uma série de número de anos transcorridos, mostre, para cada número, em qua ano o evento aconteceu. Lembre-se de indicar se ele aconteceu A.C. (Antes de Cristo) ou D.C. (Depois de Cristo).

Entrada
A entrada tem várias linhas. A primeira tem um inteiro positivo N (1 <= N <= 1000000). A seguir existem N linhas. Cada uma dessas N linhas tem um único inteio não negativo T, que indica o número de anos transcorridos até 2015 D.C. (0 <= T < 2^31).

Saída
A saída tem N linhas. Em cada uma, deve ser indicado o ano A em que o correspodente tempo T aconteceu. Veja o exemplo de saída.

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  3                               |  7986 A.C.                     |
|  10000                           |  2000 D.C.                     |
|  15                              |  1 A.C.                        |
|  2015                            |                                |
+----------------------------------+--------------------------------+
'''
n = int(input())

for i in range(n):
    t = int(input())

    if (t - 2015 >= 0):
        print(f'{(t - 2015) + 1} A.C.')
    else:
        print(f'{(2015 - t)} D.C.')