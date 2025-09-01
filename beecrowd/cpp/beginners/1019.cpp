#include <iostream>
#include <string>

int main() {
    int seg, min, hrs;
    std::cin >> seg;
    hrs = seg / 3600;
    seg %= 3600;
    min = seg / 60;
    seg %= 60;
    std::printf("%d:%d:%d\n", hrs, min, seg);
}