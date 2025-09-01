#include <iostream>

int main() {
    int n;
    std::cin >> n;

    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0) {
            std::printf("%i^2 = %i\n", i, i * i);
        }
    }
}