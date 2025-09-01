#include <iostream>

int main() {
    while (true) {
        int x, y;
        std::cin >> x >> y;

        if (x == 0 || y == 0) {
            break;
        }

        if (x > 0 && y > 0) {
            std::cout << "primeiro" << std::endl;
        } else if (x < 0 && y > 0) {
            std::cout << "segundo" << std::endl;
        } else if (x < 0 && y < 0) {
            std::cout << "terceiro" << std::endl;
        } else {
            std::cout << "quarto" << std::endl;
        }
    }
}