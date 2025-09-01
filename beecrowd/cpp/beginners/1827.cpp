#include <iostream>
#include <vector>

int main() {
    int n;
    while(std::cin >> n) {
        int s = n / 3;
        int e = n - s;

        std::vector<std::vector<int>> m(n, std::vector<int>(n, 0));

        for (int i = 0; i < n; i++) {
            m[i][i] = 2;
        }

        for (int i = 0; i < n; i++) {
            m[i][n - 1 - i] = 3;
        }

        for (int i = s; i < e; i++) {
            for (int j = s; j < e; j++) {
                m[i][j] = 1;
            }
        }

        m[n / 2][n / 2] = 4;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                std::printf("%i", m[j][i]);
            }
            std::printf("\n");
        }
        std::printf("\n");
    }
}