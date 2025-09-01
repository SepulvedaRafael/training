'''
1828 - BAZINGA!

No oitavo episodio da segunda temporada do seriado The Big Bang Theory, The Lizard-Spock Expansion, Sheldon e Raj discutem qual dos dois é o melhor: o filme Saturn 3 ou a série Deep Space 9. A sugestão de Raj para a resolução do impasse é uma disputa de Pedra-Papel-Tesoura. Contudo, Sheldon argumenta que, se as partes envolvidas se conhecem, entre 75% e 80% das dispusta de Pedra-Papel-Tesoura terminam empatadas, e então sueere o Pedra-Papel-Tesoura-Lagarto-Spock.

As regras do jogo proposto são:
1. a tesoura corta o papel;
2. o papel embrulha  a pedra;
3. a pedra esmaga o lagarto;
4. o lagarto envenena a Spock;
5. Spock destrói a tesoura;
6. a tesoura decapita o lagarto;
7. o largarto come o papel;
8. o papel contesta Spock;
9. Spock vaporiza a pedra;
10. a pedra quebra a tesoura.

Embora a situação se resolva no episodio (ambos escolhem Spock, resultam em um empate), não é difícil deduzir o que aconteceria se a disputa continuasse. Caso Sheldon vencesse, ele se deleitaria com a vitória, exclamando "Bazinga!"; caso Raj vencesse, ele concluiria que "Raj trapaceou!"; caso o resultado fosse empate, ele exigiria nova partida: "De novo!". Conhecidas as personagens do jogo escolhido por ambos, faça um programa que imprima a provável reação de Sheldon.

Entrada
A entrada consiste em uma série de casos de teste. A primeira linha contém um inteiro positivo T (T <= 100), que representa o número de casos de teste. Cada caso de teste é representado por uma linha da entrada, contendo as escolhas de Sheldon e Raj, respectivamente, separadas por um espaço em branco. As escolhas possíveis são as personagens do jogo: pedra, papel, tesoura, lagarto e Spock.

Saída
Para cada caso de teste deverá ser impressa a mensagem "Caso #t: R", onde t é o número do caso de teste (cuja constagem se inicia no número um) e R é uma das três reações possíveis de Sheldon: "Bazinga!", "Raj trapaceou!" ou "De novo!".

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  3                               |  Caso #1: Bazinga!             |
|  papel pedra                     |  Caso #2: Raj trapaceou!       |
|  lagarto tesoura                 |  Caso #3: De novo!             |
|  Spock Spock                     |                                |
+----------------------------------+--------------------------------+
'''
t = int(input())

for i in range(1, t + 1):
    case = f"Caso #{i}: "
    s, r = input().split()

    if ((s == "tesoura" and r == "papel") or (s == "papel" and r == "pedra") or (s == "pedra" and r == "lagarto") or (s == "lagarto" and r == "Spock") or (s == "Spock" and r == "tesoura") or (s == "tesoura" and r == "lagarto") or (s == "lagarto" and r== "papel") or (s == "papel" and r == "Spock") or (s == "Spock" and r == "pedra") or (s == "pedra" and r == "tesoura")):
        print(case + "Bazinga!")
    elif ((s == "papel" and r == "papel") or (s == "pedra" and r == "pedra") or (s == "tesoura" and r == "tesoura") or (s == "lagarto" and r == "lagarto") or (s == "Spock" and r == "Spock")):
        print(case + "De novo!")
    else:
        print(case + "Raj trapaceou!")
