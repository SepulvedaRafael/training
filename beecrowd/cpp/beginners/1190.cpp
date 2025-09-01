#include <iostream>

int main() {
    char operacao;
    std::cin >> operacao;
    double matriz[12][12];

    for (int i = 0; i < 12; i++) {
        for (int j = 0; j < 12; j++) {
            double valor;
            std::cin >> valor;
            matriz[i][j] = valor;
        }
    }

    double soma = 0.0;
    for (int i = 0; i < 12; i++) {
        for (int j = 0; j < 12; j++) {
            if (i >= 1 && i <= 10 && j >= 12 - i && i < j) {
                soma += matriz[i][j];
            }
        }
    }

    if (operacao == 'S') {
        std::printf("%.1f\n", soma);
    } else {
        std::printf("%.1f\n", soma / 12);
    }
}