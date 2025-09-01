#include <iostream>

int main() {
    int v;
    std::cin >> v;

    for (int i = 0; i < 10; i++) {
        std::printf("N[%i] = %i\n", i, v);
        v = v * 2;
    }
}