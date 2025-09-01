#include <iostream>
#include <iomanip>
#include <string>

int main() {
    std::string name;
    double salary, montant;
    std::cin >> name >> salary >> montant;
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "TOTAL = R$ " << (0.15 * montant) + salary << std::endl;
}