#include <iostream>
#include <iomanip>
#include <cmath>

int main() {
    double x1, x2, y1, y2;
    std::cin >> x1 >> y1;
    std::cin >> x2 >> y2;
    std::cout << std::fixed << std::setprecision(4);
    std::cout << std::sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)) << std::endl;
}