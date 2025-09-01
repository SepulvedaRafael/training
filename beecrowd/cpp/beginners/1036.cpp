#include <iostream>
#include <cmath>

int main() {
    double a, b, c, x1, x2, delta;
    std::cin >> a >> b >> c;
    delta = std::pow(b, 2) - (4 * a * c);

    if (a <= 0.0 || delta <= 0.0) {
        std::cout << "Impossivel calcular" << std::endl;
    } else {
        x1 = (-b + std::sqrt(delta)) / (2 * a);
        x2 = (-b - std::sqrt(delta)) / (2 * a);
        std::printf("R1 = %.5f\n", x1);
        std::printf("R2 = %.5f\n", x2);
    }
}