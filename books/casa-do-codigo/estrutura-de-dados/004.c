/*
4) Faça um programa com uma matriz com 9 elementos (3x3) reais positivos (aleatórios e de sua escolha). Calcule e exiba a soma dos elementos de cada linha desta matriz.
*/

#include <stdio.h>

int main() {
    float numeros[3][3] = {
        {1.5, 6.3, 8.9},
        {2.6, 9.5, 1.2},
        {3.4, 7.5, 4.9}
    };

    for (int i = 0; i < 3; i++) {
        float soma = 0.0;
        for (int j = 0; j < 3; j++) {
            soma += numeros[i][j];
        }
        printf("A soma dos elementos da Linha %i = %.2f\n", i, soma);
    }

    return 0;
}