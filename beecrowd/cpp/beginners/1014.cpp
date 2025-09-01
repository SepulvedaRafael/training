#include <iostream>
#include <iomanip>

int main() {
    int totalDistanceTraveled;
    double totalFuelSpent;
    std::cin >> totalDistanceTraveled >> totalFuelSpent;
    std::cout << std::fixed << std::setprecision(3);
    std::cout << totalDistanceTraveled / totalFuelSpent << " km/l" << std::endl;
}