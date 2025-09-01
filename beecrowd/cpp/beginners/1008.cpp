#include <iostream>
#include <iomanip>

int main() {
    int number, hoursWorked;
    double salary;
    std::cin >> number >> hoursWorked >> salary;
    std::cout << "NUMBER = " << number;
    std::cout << std::fixed << std::setprecision(2) << std::endl;
    std::cout << "SALARY = U$ " << hoursWorked * salary << std::endl;
}