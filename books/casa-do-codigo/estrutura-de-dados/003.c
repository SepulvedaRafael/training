/*
3) Faça um programa com um vetor com 10 elementos inteiros positivos (aleatórios e de sua escolha). Permita que seja solicitado um determinado valor inteiro e positivo para ser procurado neste vetor. Caso exista, o programa deve exibir o índice no qual o valor está posicionado. Caso contrário, o programa deve informar que o elemento não existe no vetor.
*/

#include <stdio.h>

int main() {
    int numeros[10] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    int numero_procurado;
    int indice = 0;

    printf("Numero a ser procurado: ");
    scanf("%i", &numero_procurado);

    size_t length = sizeof(numeros) / sizeof(numeros[0]);
    for (size_t i = 0; i < length; i++) {
        if (numeros[i] == numero_procurado) {
            indice = i;
        }
    }

    if (indice == 0) {
        printf("Numero nao foi encontrado!");
    } else {
        printf("numeros[%i] = %i", indice, numero_procurado);
    }

    return 0;
}