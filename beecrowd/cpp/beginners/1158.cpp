#include <iostream>

int main() {
    int cases;
    std::cin >> cases;

    for (int i = 0; i < cases; i++) {
        int x, y;
        std::cin >> x >> y;

        int cont = 0;
        int soma = 0;
        while (cont != y) {
            if (x % 2 != 0) {
                soma += x;
                cont++;
            }

            x++;
        }

        std::cout << soma << std::endl;
    }
}