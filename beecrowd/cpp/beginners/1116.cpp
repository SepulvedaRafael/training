#include <iostream>

int main() {
    int cases;
    std::cin >> cases;

    for (int i = 0; i < cases; i++) {
        double x, y;
        std::cin >> x >> y;

        if (y == 0) {
            std::cout << "divisao impossivel" << std::endl;
        } else {
            std::printf("%.1f\n", x / y);
        }
    }
}