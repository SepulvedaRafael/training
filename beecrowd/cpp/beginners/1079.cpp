#include <iostream>

int main() {
    int n;
    float num1, num2, num3;

    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::cin >> num1 >> num2 >> num3;
        std::printf("%.1f\n", ((num1 * 2) + (num2 * 3) + (num3 * 5)) / 10);
    }
}