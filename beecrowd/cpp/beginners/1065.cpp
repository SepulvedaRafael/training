#include <iostream>
#include <vector>

int main() {
    int num1, num2, num3, num4, num5;
    std::cin >> num1 >> num2 >> num3 >> num4 >> num5;
    std::vector<int> nums = {num1, num2, num3, num4, num5};

    int cont = 0;
    for (int num : nums) {
        (num % 2 == 0) ? cont++ : 0;
    }

    std::printf("%i valores pares\n", cont);
}