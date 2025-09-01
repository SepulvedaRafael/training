#include <iostream>
#include <vector>

int main() {
    double num1, num2, num3, num4, num5, num6;
    std::cin >> num1 >> num2 >> num3 >> num4 >> num5 >> num6;
    std::vector<double> nums = {num1, num2, num3, num4, num5, num6};

    double sum = 0;
    int cont = 0;
    for (size_t i = 0; i < nums.size(); ++i) {
        if (nums[i] >= 0){
            sum += nums[i];
            cont++;
        }
    }

    std::printf("%d valores positivos\n", cont);
    std::printf("%.1f\n", sum / cont);
}