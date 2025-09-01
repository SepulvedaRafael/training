#include <iostream>

int main() {
    while (true) {
        int m, n;
        std::cin >> m >> n;

        if (m <= 0 || n <= 0) {
            break;
        }

        int sum = 0;
        if (m > n) {
            for (int i = n; i <= m; i++) {
                std::printf("%d ", i);
                sum += i;
            }
            std::printf("Sum=%i\n", sum);
        } else {
            for (int i = m; i <= n; i++) {
                std::printf("%d ", i);
                sum += i;
            }
            std::printf("Sum=%i\n", sum);
        }
    }
}