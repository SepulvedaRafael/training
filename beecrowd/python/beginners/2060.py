'''
2060 - DESAFIO DE BINO

Bino e Cino são colegas inseparáveis. Bino gosta de criar desafios matemáticos para Cino resolver. Desta vez, Bino gerou uma lista de números e perguntou ao Cino quantos números da lista são múltiplos de 2, 3, 4 e 5.

Esse desafio pode parecer simples, porém, quando a lista contém muitos números, Cino se confunde e acaba errando alguns cálculos. Para ajudar Cino, faça um programa para resolver o desafio de Bino.

Entrada
A primeira linha da entrada consiste em um inteiro N (1 ≤ N ≤1000), representando a quantidade de números na lista de Bino.

A segunda linha contém N inteiros Li (1 ≤ Li ≤ 100), representando os números da lista de Bino.

Saída
Imprima a quantidade de números múltiplos de 2, 3, 4 e 5 presentes na lista. Observe a formatação da saída nos exemplos, pois ela deve ser seguida rigorosamente.

+----------------------------------+--------------------------------+
|        Exemplo de Entrada        |       Exemplo de Saída         |
+----------------------------------+--------------------------------+
|  5                               |  4 Multiplo(s) de 2            |
|  2 5 4 20 10                     |  0 Multiplo(s) de 3            |
|                                  |  2 Multiplo(s) de 4            |
|                                  |  3 Multiplo(s) de 5            |
+----------------------------------+--------------------------------+
'''
n = int(input())
l = list(map(int, input().split()))

multiplos = []
for i in range(2, 6):
    contador = 0
    for num in l:
        if (num % i == 0):
            contador += 1
    multiplos.append(contador)

print(f"{multiplos[0]} Multiplo(s) de 2")
print(f"{multiplos[1]} Multiplo(s) de 3")
print(f"{multiplos[2]} Multiplo(s) de 4")
print(f"{multiplos[3]} Multiplo(s) de 5")