#include <iostream>

int main() {
    int t;
    std::cin >> t;

    int aux = 0;
    for (int i = 0; i < 1000; i++) {
        std::printf("N[%i] = %i\n", i, aux);
        aux++;

        if (aux == t) {
            aux = 0;
        }
    }
}