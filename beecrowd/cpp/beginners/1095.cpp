#include <iostream>

int main() {
    int i = 1;
    for (int j = 60; j >= 0; j = j - 5) {
        std::printf("I=%i J=%i\n", i, j);
        i = i + 3;
    }
}