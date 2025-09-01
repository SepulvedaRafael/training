/*
5) Faça um programa com uma matriz 5x5 de inteiros positivos ou negativos (aleatórios e de sua escolha) e encontre e exiba o maior elemento desta matriz.
*/

#include <stdio.h>

int main() {
    int rows = 5;
    int cols = 5;
    float numeros[5][5] = {
        {1.5, 6.3, 8.9, -2.3, -4.1},
        {2.6, 9.5, 1.2, 5.3, -9.2},
        {3.4, 7.5, 4.9, -0.4, -6.2},
        {2.3, 5.6, 4.3, 7.8, 9.8},
        {-7.5, -3.2, -6.5, -3.1, -9.6}
    };

    float max = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (numeros[i][j] > max) {
                max = numeros[i][j];
            }
        }
    }

    printf("O maior elemento encontrado foi: %.2f", max);

    return 0;
}