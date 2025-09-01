'''
2139 - NATAL DE PEDRINHO

Pedrinho é um garoto que adora festas em família, principalmente o Natal, quando ganha presente dos pais e dos avós. Esse ano, seu pai lhe prometeu um PS4, mas somente se Pedrinho conseguir resolver alguns desafios ao longo do ano, sendo um deles, escrever um programa que calcule quantos dias faltam para o Natal.

Entretanto, Pedrinho tem somente 9 anos e não tem noção alguma de programação, mas sabe que você, primo dele, mexe com "coisas de computador", e dessa forma, pediu para você escrever o programa para ele. Não somente isso, mas prometeu que deixaria você jogar todo final de semana e por quanto tempo quiser!

Entrada
A entrada é composta por vários casos de teste. Cada linha contém o mês e o dia do ano de 2016 (ano bissexto). A entrada termina com fim de arquivo.

Saída
Se for Natal, imprima "E natal!"; se faltar somente um dia, imprima "E vespera de natal!"; se já passou, imprima "Ja passou!". Caso contrário, imprima "Faltam X dias para o natal!", sendo X o número de dias que faltam para o Natal.

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  12 24                           |  E vespera de natal!           |
|  11 24                           |  Faltam 31 dias para o natal!  |
|  12 29                           |  Ja passou!                    |
|  1 5                             |  Faltam 355 dias para o natal! |
|  12 25                           |  E natal!                      |
+----------------------------------+--------------------------------+
'''
while True:
    try:
        dias_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 25]
        mes, dias = map(int, input().split())

        total_dias = sum(i for i in dias_mes)

        qtd_dias = 0
        for i, dia in enumerate(dias_mes, start=1):
            if i < mes:
                qtd_dias += dia

            elif i == mes:
                qtd_dias += dias

        if total_dias - qtd_dias > 1:
            print(f'Faltam {total_dias - qtd_dias} dias para o natal!')
        elif total_dias - qtd_dias == 1:
            print('E vespera de natal!')
        elif total_dias - qtd_dias == 0:
            print('E natal!')
        else:
            print('Ja passou!')
    except EOFError:
        break