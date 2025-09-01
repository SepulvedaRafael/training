#include <iostream>

int main() {
    int days, months, years;
    std::cin >> days;

    years = days / 365;
    days %= 365;
    months = days / 30;
    days %= 30;
    std::cout << years << " ano(s)" << std::endl;
    std::cout << months << " mes(es)" << std::endl;
    std::cout << days << " dia(s)" << std::endl;
}