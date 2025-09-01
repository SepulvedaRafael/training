#include <iostream>
#include <cmath>

int main() {
    int a, b, c;
    std::cin >> a >> b >> c;
    int maiorAB = (a + b + std::abs(a - b)) / 2;
    int maior = (maiorAB + c + std::abs(maiorAB - c)) / 2;
    std::cout << maior << " eh o maior" << std::endl;
}