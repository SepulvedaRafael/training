#include <iostream>

int main() {
    int n;
    std::cin >> n;

    for (int i = 1; i <= n; i++) {
        if (i == n) {
            std::printf("Ho!\n");
        } else {
            std::printf("Ho ");
        }
    }
}