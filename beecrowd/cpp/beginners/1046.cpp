#include <iostream>

int main() {
    int hourI, hourF, duration;
    std::cin >> hourI >> hourF;

    if (hourI > hourF) {
        duration = (24 - hourI) + hourF;
    } else if (hourI == hourF) {
        duration = 24;
    } else {
        duration = hourF - hourI;
    }

    std::printf("O JOGO DUROU %i HORA(S)\n", duration);
}