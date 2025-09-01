#include <iostream>

int main() {
    int tipo;
    const int length = 5;
    int nums[length];
    std::cin >> tipo;

    for (int i = 0; i < length; i++) {
        std::cin >> nums[i];
    }

    int cont = 0;
    for (int i = 0; i < length; i++) {
        if (nums[i] == tipo) {
            cont++;
        }
    }

    std::cout << cont << std::endl;
}