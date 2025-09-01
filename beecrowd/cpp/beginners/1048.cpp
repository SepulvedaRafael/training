#include <iostream>

int main() {
    double salary, new_salary, readjustment, percentual;
    std::cin >> salary;

    if (salary <= 400.00) {
        percentual = 0.15;
    } else if (salary > 400.00 && salary <= 800.00) {
        percentual = 0.12;
    } else if (salary > 800.00 && salary <= 1200.00) {
        percentual = 0.10;
    } else if (salary > 1200.00 && salary <= 2000.00) {
        percentual = 0.07;
    } else {
        percentual = 0.04;
    }

    readjustment = salary * percentual;
    new_salary = salary + readjustment;

    std::printf("Novo salario: %.2f\n", new_salary);
    std::printf("Reajuste ganho: %.2f\n", readjustment);
    std::printf("Em percentual: %.0f %\n", percentual * 100);
}