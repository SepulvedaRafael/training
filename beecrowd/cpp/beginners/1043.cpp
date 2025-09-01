#include <iostream>

int main() {
    double a, b, c;
    std::cin >> a >> b >> c;

    if (a + b > c && a + c > b && b + c > a) {
        std::printf("Perimetro = %.1f\n", a + b + c);
    } else {
        std::printf("Area = %.1f\n", ((a+b) * c) / 2);
    }
}