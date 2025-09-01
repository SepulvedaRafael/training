'''
2126 - PROCURANDO SUBSEQUÊNCIAS

Dados dois números naturais N1 e N2, diz-se que N1 é subsequência contígua de N2 se todos os dígitos de N1 aparecem, na mesma ordem e de forma contígua, em N2. Crie uma aplicação que leia dois números naturais e diga se o primeiro é uma subsequência contígua do segundo.

Entrada
A entrada é composta por vários casos de teste e termina com final de arquivo (EOF). A primeira linha de cada entrada é composta por um valor natural N1(1 < N1 < 1010), a segunda linha é composta por um valor N2( N1 < N2 < 1032).

Saída
Para cada caso de teste imprima a quantidade de subsequências contíguas e a posição onde a subsequência é iniciada, caso exista mais de uma subsequência, imprima onde é iniciada a última subsequência. Caso não exista subsequência, imprima "Nao existe subsequencia". Mostre o resultado conforme o exemplo de saída.

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  78954                           |  Caso #1:                      |
|  7895478954789547895447895478954 |  Qtd.Subsequencias: 6          |
|  464133                          |  Pos: 27                       |
|  1331646546874694                |                                |
|  12                              |  Caso #2:                      |
|  1231321455123214565423112       |  Nao existe subsequencia       |
|                                  |                                |
|                                  |  Caso #3:                      |
|                                  |  Qtd.Subsequencias: 3          |
|                                  |  Pos: 24                       |
+----------------------------------+--------------------------------+
'''
contador = 1
while True:
    try:
        n1 = int(input())
        n2 = int(input())

        print(f'Caso #{contador}')

        subsequencias = str(n2).count(str(n1))
        if subsequencias > 0:
            print(f'Qtd.subsequencias: {subsequencias}')
            print(f'Pos: {str(n2).rfind(str(n1)) + 1}\n')
        else:
            print('Não existe subsequencia\n')

        contador += 1
    except EOFError:
        break