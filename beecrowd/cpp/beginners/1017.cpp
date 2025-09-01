#include <iostream>
#include <iomanip>

int main() {
    double timeSpent, averageSpeed;
    std::cin >> timeSpent >> averageSpeed;
    std::cout << std::fixed << std::setprecision(3);
    std::cout << (averageSpeed * timeSpent) / 12 << std::endl;
}