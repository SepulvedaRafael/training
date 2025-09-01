#include <iostream>

int main() {
    int a, b;
    std::cin >> a >> b;

    if (b > a) {
        b % a == 0 ? std::cout << "Sao Multiplos" << std::endl : std::cout << "Nao sao Multiplos" << std::endl;
    } else {
        a % b == 0 ? std::cout << "Sao Multiplos" << std::endl : std::cout << "Nao sao Multiplos" << std::endl;
    }
}