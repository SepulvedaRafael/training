#include <iostream>

int main() {
    int hourI, minI, hourF, minF, initI, initF, duration, hours, mins;
    std::cin >> hourI >> minI >> hourF >> minF;

    initI = (hourI * 60) + minI;
    initF = (hourF * 60) + minF;

    if (initF > initI) {
        duration = initF - initI;
    } else if (initI > initF) {
        duration = (24 * 60 - initI) + initF;
    } else {
        duration = 24 * 60;
    }

    hours = duration / 60;
    mins = duration % 60;

    std::printf("O JOGO DUROU %i HORA(S) E %i MINUTO(S)\n", hours, mins);
}