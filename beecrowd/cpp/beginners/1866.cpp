#include <iostream>

int main() {
    int cases;
    std::cin >> cases;

    for (int i = 0; i < cases; i++) {
        int n;
        std::cin >> n;

        int soma = 0;
        for (int j = 0; j < n; j++) {
            if (j % 2 == 0) {
                soma += 1;
            } else {
                soma -= 1;
            }
        }
        std::printf("%i\n", soma);
    }
}