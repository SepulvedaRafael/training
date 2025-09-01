#include <iostream>

int main() {
    double salary;
    std::cin >> salary;

    double tax = 0;

    if (salary <= 2000.00) {
        std::cout << "Isento" << std::endl;
    } else {
        if (salary > 2000.00 && salary <= 3000.00)
        {
            tax += (salary - 2000) * 0.08;
        }
        else if (salary > 3000.00)
        {
            tax += 1000 * 0.08;
        }

        if (salary > 3000.00 && salary <= 4500.00)
        {
            tax += (salary - 3000) * 0.18;
        }
        else if (salary > 4500.00)
        {
            tax += 1500 * 0.18;
        }

        if (salary > 4500.00)
        {
            tax += (salary - 4500) * 0.28;
        }

        std::printf("R$ %.2f\n", tax);
    }
}