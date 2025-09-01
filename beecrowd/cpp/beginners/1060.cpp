#include <iostream>

int main() {
    double num1, num2, num3, num4, num5, num6;
    std::cin >> num1 >> num2 >> num3 >> num4 >> num5 >> num6;
    double nums[6] = {num1, num2, num3, num4, num5, num6};

    int cont = 0;
    for (double num : nums) {
        if (num > 0) {
            cont++;
        }
    }

    std::cout << cont << " valores positivos" << std::endl;
}