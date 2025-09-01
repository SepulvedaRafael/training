#include <iostream>

int main() {
    int i = 1;
    while (i <= 9) {
        for (int j = 7; j >= 5; j--) {
            std::printf("I=%i J=%i\n", i, j);
        }
        i += 2;
    }
}