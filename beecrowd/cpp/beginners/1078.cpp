#include <iostream>

int main() {
    int n;
    std::cin >> n;

    for (int i = 1; i <= 10; i++) {
        std::printf("%i x %i = %i\n", i, n, i * n);
    }
}