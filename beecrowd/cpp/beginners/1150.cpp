#include <iostream>

int main() {
    int x, z;
    std::cin >> x;

    while (true) {
        std::cin >> z;
        if (z > x) {
            break;
        }
    }

    int soma = 0;
    int cont = 0;
    while (soma < z) {
        soma += x + cont;
        cont++;
    }

    std::cout << cont << std::endl;
}