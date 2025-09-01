#include <iostream>

int main() {
    int cont = 0;
    double soma = 0.0;
    while (true) {
        double nota;
        std::cin >> nota;

        if (nota < 0 || nota > 10) {
            std::cout << "nota invalida" << std::endl;
        } else {
            soma += nota;
            cont++;

            if (cont == 2) {
                break;
            }
        }
    }

    std::printf("media = %.2f\n", soma / 2.0);
}