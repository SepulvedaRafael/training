#include <iostream>

int main() {
    while (true) {
        int x, y;
        std::cin >> x >> y;

        if (x == y) {
            break;
        }

        (x > y) ? std::cout << "Decrescente" << std::endl : std::cout << "Crescente" << std::endl;
    }
}