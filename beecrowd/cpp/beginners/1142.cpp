#include <iostream>

int main() {
    int n;
    std::cin >> n;

    int last_value = 0;
    for (int i = 0; i < n; i++) {
        int diff = last_value + 3;
        for (int j = last_value + 1; j <= diff; j++) {
            std::printf("%i ", j);
            if (j == diff) {
                last_value = j + 1;
                break;
            }
        }
        std::printf("PUM\n");
    }
}