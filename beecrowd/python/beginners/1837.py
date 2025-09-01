'''
1837 - PREFÁCIO

Começou a 4a Maratora de Programação da UFFS! Esperamos que você aproveite as próximas horas que passará conosco e que se divirta muito! Boa sorte!

Este é o 3o ano de Clube de Programação, projeto de extensão que visa em primeiro lugar tornar os programadores da região brasileira conehcida como Fronteira Sul muito aptos a enfrentar os desafios computacionais tanto da academia quanto do mercado de trabalho. Nossa principal estratégia está em promover oficinas e treinos para competições de Programação, não apenas para estudantes da UFFS, mas para quem quiser participar. Apesar das várias dificuldades, estamos muito felizes com os resultados que temos conquistado. Em parceria com a UNOCHAPECÓ, a URI e a UNOESC, colaboramos para fazer de Chapecó nos dois últimos anos a 2a maior sede do Brasil na etapa regional da Maratona de Programação, o que é mais um indicador do entusiamo que o povo daqui tem por Programação.

Para aquecer você para esta comeptição, vamos pedir que você desenvolva um programa que calcule o quociente e o resto da divisão de dois números inteiros, pode ser? Lembre que o quociente e o resto da divisão de um inteiro a por um inteiro não-nulo b são respectivamente os únicos inteiros q e r tais que 0 <= r < |b| e:

a = b x q + r

Caso você não saiba, o teorema que garante a existência e a unicidade dos inteiros q e r é conhecido como "Teorema da Divisão Euclidiana" ou "Algoritmo da Divisão".

Entrada
A entrada é composta por dois números inteiros a e b (-1.000 <= a, b < 1.000).

Saída
Imprima o quociente q seguido pelo resto r da divisão de a por b.

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  7 3                             |  2 1                           |
+----------------------------------+--------------------------------+

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  7 -3                            |  -2 1                          |
+----------------------------------+--------------------------------+

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  -7 3                            |  -3 2                          |
+----------------------------------+--------------------------------+
'''
a, b = map(int, input().split())

r = (a % b)
q = (a // b)
if r < 0:
    r = r + abs(b)
    q = (a - r) // b
    print(f"{q:.0f} {r}")
else:
    print(f"{q} {r}")