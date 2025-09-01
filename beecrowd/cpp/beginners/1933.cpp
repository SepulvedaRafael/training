#include <iostream>

int main() {
    int a, b;
    std::cin >> a >> b;

    if (a > b) {
        std::cout << a << std::endl;
    } else if (a < b) {
        std::cout << b << std::endl;
    } else {
        std::cout << a << std::endl;
    }
}