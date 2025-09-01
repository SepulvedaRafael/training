#include <iostream>
#include <algorithm>
#include <cmath>

int main() {
    double a, b, c;
    std::cin >> a >> b >> c;
    double nums[] = {a, b, c};
    std::sort(nums, nums + 3);
    std::reverse(nums, nums + 3);
    a = nums[0];
    b = nums[1];
    c = nums[2];

    if (a >= b + c) {
        std::cout << "NAO FORMA TRIANGULO" << std::endl;
    } else {
        if (a * a == (b * b) + (c * c)) {
            std::cout << "TRIANGULO RETANGULO" << std::endl;
        }
        if (a * a > (b * b) + (c * c)) {
            std::cout << "TRIANGULO OBTUSANGULO" << std::endl;
        }
        if (a * a < (b *b) + (c * c)) {
            std::cout << "TRIANGULO ACUTANGULO" << std::endl;
        }
        if (a == b && b == c) {
            std::cout << "TRIANGULO EQUILATERO" << std::endl;
        }
        if ((a == b && b != c) || (b == c && c != a) || (a == c && c != b)) {
            std::cout << "TRIANGULO ISOSCELES" << std::endl;
        }
    }
}