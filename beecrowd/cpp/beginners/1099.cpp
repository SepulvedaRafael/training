#include <iostream>

int main() {
    int cases;
    std::cin >> cases;

    for (int i = 0; i < cases; i++) {
        int x, y;
        std::cin >> x >> y;

        int sum = 0;
        if (x > y) {
            for (int i = y + 1; i < x; i++) {
                if (i % 2 != 0) {
                    sum += i;
                }
            }
        } else if (x == y) {
            sum = 0;
        } else {
            for (int i = x + 1; i < y; i++) {
                if (i % 2 != 0) {
                    sum += i;
                }
            }
        }
        std::cout << sum << std::endl;
    }
}