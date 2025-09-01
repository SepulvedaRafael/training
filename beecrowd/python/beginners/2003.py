'''
2003 - DOMINGO DE MANHÃ

Domingo é dia de feira. Logo de manhã mutias pessoas se deslocam para o polo de lazer da Parangaba, onde acontece uma feira, conhecida por ser a maior da cidade. Na feira da Parangaba você pode encontrar de tudo.

Todos os domingos, Bino faz compras na feira. Ele sempre marca com seu amigo Cino de se encontrarem no terminal de ônibus da Parangaba às 8h, para irem juntos comprar na feira. Porém, muitas vezes Bino acorda muito tarde e se atrasa para o encontro com seu amigo.

Sabendo que Bino leva de 30 a 60 minutos para chegar ao terminal. Diga o atraso máximo de Bino.

Entrada
A entrada consiste em múltiplos casos teste. Cada caso de teste contém uma única linha contendo um horário H (5:00 <= H <= 9:00) que Bino acordou. A entrada termina com final de arquivo (EOF).

Saída
Para cada caso de teste, impriva "Atraso máximo: X" (sem aspas), X indicando o atraso máximo (em minutos) de Bino no encontro com Cino.

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  7:10                            |  Atraso maximo: 10             |
|  5:00                            |  Atraso maximo: 0              |
+----------------------------------+--------------------------------+
'''
while True:
    try:
        hora, minutos = map(int, input().split(':'))

        if (hora < 7):
            print(f'Atraso maximo {0}')
        elif (hora == 7):
            print(f'Atraso maximo: {minutos}')
        elif (hora == 9):
            mins = 120 + minutos
            print(f'Atraso maximo: {mins}')
        else:
            mins = 60 + minutos
            print(f'Atraso maximo: {mins}')
    except EOFError:
        break