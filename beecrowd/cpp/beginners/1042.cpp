#include <iostream>
#include <algorithm>

int main() {
    int n1, n2, n3, i;
    std::cin >> n1 >> n2 >> n3;
    int nums[] = {n1, n2, n3};
    i = sizeof(nums) / sizeof(nums[0]);
    std::sort(nums, nums + i);

    for (int j = 0; j < i; ++j) {
        std::cout << nums[j] << std::endl;
    }
    std::cout << std::endl;
    std::cout << n1 << std::endl;
    std::cout << n2 << std::endl;
    std::cout << n3 << std::endl;
}