#include <iostream>
#include <iomanip>

int main() {
    while (true) {
        int n;
        std::cin >> n;

        if (n == 0) {
            break;
        }

        int elemento = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (i == j) {
                    elemento = 1;
                } else if (i > j) {
                    elemento = i - j + 1;
                } else {
                    elemento = j - i + 1;
                }

                std::cout << std::setw(3) << elemento;
                if (j != n) {
                    std::printf(" ");
                }
            }
            std::printf("\n");
        }
        std::printf("\n");
    }
}