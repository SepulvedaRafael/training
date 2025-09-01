#include <iostream>
#include <cstring>

int main() {
    int cases;
    std::cin >> cases;

    for (int i = 0; i < cases; i++) {
        char heroi[20];
        int poder;

        std::cin >> heroi >> poder;

        // strcmp compara duas strings e retorna 0 (iguais), neg (menor), pos (maior)
        (std::strcmp(heroi, "Thor") == 0) ? std::printf("Y\n") : std::printf("N\n");
    }
}