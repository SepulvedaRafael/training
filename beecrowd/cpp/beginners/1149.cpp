#include <iostream>

int main() {
    int a, n;
    std::cin >> a;

    while (true) {
        std::cin >> n;
        if (n > 0) {
            break;
        }
    }

    int soma = 0;
    for (int i = 0; i < n; i++) {
        soma += a + i;
    }

    std::cout << soma << std::endl;
}