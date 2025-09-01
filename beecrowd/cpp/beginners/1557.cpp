#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>

int main() {
    int n;
    while (std::cin >> n && n != 0) {
        // Matriz n x n inicializada com 0
        std::vector<std::vector<int>> m(n, std::vector<int>(n, 0));

        // Inserir os elementos conforme a lógica
        m[0][0] = 1;
        for (int i = 0; i < n; i++) {
            if (i >= 1) {
                m[i][0] = m[i - 1][0] * 2;
            }

            for (int j = 1; j < n; j++) {
                m[i][j] = m[i][j - 1] * 2;
            }
        }

        // Determinar o número de dígitos do maior número
        int max_val = m[n - 1][n - 1];
        int T = std::to_string(max_val).length();

        // Imprimir a matriz formatada
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (j != 0) {
                    std::cout << " ";
                }
                std::cout << std::setw(T) << m[i][j];
            }
            std::cout << std::endl;
        }
        std::cout << std::endl;
    }
}