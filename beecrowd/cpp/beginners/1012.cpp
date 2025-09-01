#include <iostream>
#include <iomanip>

int main() {
    double a, b, c;
    double PI = 3.14159;
    std::cin >> a >> b >> c;
    std::cout << std::fixed << std::setprecision(3);
    std::cout << "TRIANGULO: " << (a * c) / 2 << std::endl;
    std::cout << "CIRCULO: " << PI * (c * c) << std::endl;
    std::cout << "TRAPEZIO: " << ((a + b) * c) / 2 << std::endl;
    std::cout << "QUADRADO: " << b * b << std::endl;
    std::cout << "RETANGULO: " << a * b << std::endl;
}