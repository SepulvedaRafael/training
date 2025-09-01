#include <iostream>

int main() {
    int cont = 0;
    double soma = 0.0;
    while (true) {
        int idade;
        std::cin >> idade;

        if (idade < 0) {
            break;
        }

        soma += idade;
        cont ++;
    }

    std::printf("%.2f\n", soma / cont);
}