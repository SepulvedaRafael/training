#include <iostream>

int main() {
    int x;
    std::cin >> x;

    int cont = 0;
    while (cont < 6) {
        if (x % 2 != 0) {
            std::cout << x << std::endl;
            cont++;
        }
        x++;
    }
}