#include <iostream>

int main() {
    int cases, x;
    std::cin >> cases;

    int in = 0, out = 0;
    for (int i = 0; i < cases; i++) {
        std::cin >> x;
        (x >= 10 && x <= 20) ? in++ : out++;
    }

    std::printf("%i in\n", in);
    std::printf("%i out\n", out);
}