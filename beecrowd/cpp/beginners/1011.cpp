#include <iostream>
#include <iomanip>
#include <cmath>

int main() {
    double PI = 3.14159;
    double raio;
    std::cin >> raio;
    std::cout << std::fixed << std::setprecision(3);
    std::cout << "VOLUME = " << (4.0/3) * PI * std::pow(raio, 3.0) << std::endl;
}