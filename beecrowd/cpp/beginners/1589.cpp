#include <iostream>

int main() {
    int cases;
    std::cin >> cases;

    for (int i = 0; i < cases; i++) {
        int r1, r2;
        std::cin >> r1 >> r2;

        std::cout << r1 + r2 << std::endl;
    }
}