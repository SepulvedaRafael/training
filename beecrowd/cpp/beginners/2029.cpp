#include <iostream>

int main() {
    const int PI = 3.14;
    double volume, diametro;
    while (std::cin >> volume && std::cin >> diametro) {
        double raio = diametro / 2;
        double areaBase = PI * (raio * raio);
        double altura = volume / areaBase;

        std::printf("ALTURA = %.2f\n", altura);
    }
}