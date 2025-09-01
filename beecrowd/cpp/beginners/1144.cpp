#include <iostream>

int main() {
    int n;
    std::cin >> n;

    for (int i = 1; i <= n; i++) {
        int j = i * i;
        int k = j * i;
        std::printf("%i %i %i\n", i, j, k);
        std::printf("%i %i %i\n", i, j+1, k+1);
    }
}