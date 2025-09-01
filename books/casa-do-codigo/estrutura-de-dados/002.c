/*
1) Crie uma matriz de caracteres (char) de 16 posições (4x4). Preencha-a com os valores a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p. Use dois for para exibir os valores desta matriz.
*/

#include <stdio.h>

int main() {
    char letras[4][4] = {
        {'A', 'B', 'C', 'D'},
        {'E', 'F', 'G', 'H'},
        {'I', 'J', 'K', 'L'},
        {'M', 'N', 'O', 'P'}
    };

    printf("Your letters: ");
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            printf("%c ", letras[i][j]);
        }
    }

    return 0;
}