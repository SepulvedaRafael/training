#include <iostream>

int main() {
    int n;
    std::cin >> n;

    int fat = 1;
    for (int i = n; i >= 1; i--) {
        fat *= i;
    }

    std::cout << fat << std::endl;
}