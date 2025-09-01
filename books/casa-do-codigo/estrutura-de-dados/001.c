/*
1) Crie um vetor de inteiros (int) de 10 posições. Preencha-o com os valores 10, 20, 30, 40, 50, 60, 70, 80, 90, 100. Use um for para exibir os valores deste vetor.
*/

#include <stdio.h>

int main() {
    int numeros[10] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};

    printf("Your numbers: ");
    for (int i = 0; i < 10; i++) {
        printf("%i ", numeros[i]);
    }

    return 0;
}