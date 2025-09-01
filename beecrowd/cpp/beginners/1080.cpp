#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int num;
    std::vector <int> nums;

    for (int i = 0; i < 100; i++) {
        std::cin >> num;
        nums.push_back(num);
    }

    int max = *std::max_element(nums.begin(), nums.end());
    std::cout << max << std::endl;

    auto it = std::find(nums.begin(), nums.end(), max);
    if (it != nums.end()) {
        std::cout << std::distance(nums.begin(), it) + 1 << std::endl;
    }
}