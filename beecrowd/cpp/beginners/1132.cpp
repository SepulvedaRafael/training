#include <iostream>

int main() {
    int x, y;
    std::cin >> x >> y;

    int soma = 0;
    if (x > y) {
        for (int i = y; i <= x; i++) {
            if (i % 13 != 0) {
                soma += i;
            }
        }
    } else if (x < y) {
        for (int i = x; i <= y; i++) {
            if (i % 13 != 0) {
                soma += i;
            }
        }
    }

    std::cout << soma << std::endl;
}