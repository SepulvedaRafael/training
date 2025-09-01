#include <iostream>
#include <cstdio>

int main() {
    char _[3];
    int dayI, dayF;
    int hourI, minuteI, secondI;
    int hourF, minuteF, secondF;

    std::scanf("%3s %d", _, &dayI);
    std::scanf("%d : %d : %d", &hourI, &minuteI, &secondI);

    std::scanf("%3s %d", _, &dayF);
    std::scanf("%d : %d : %d", &hourF, &minuteF, &secondF);

    int durationI = (dayI * 86400) + (hourI * 3600) + (minuteI * 60) + secondI;
    int durationF = (dayF * 86400) + (hourF * 3600) + (minuteF * 60) + secondF;

    int duration = 0;
    if (durationF > durationI) {
        duration = durationF - durationI;
    } else if (durationI > durationF) {
        duration = (24 * 60 - durationI) + durationF;
    } else {
        duration = (24 * 60);
    }

    int days = duration / 86400;
    int seconds = duration % 86400;
    int hours = seconds / 3600;
    seconds = duration % 3600;
    int minutes = seconds / 60;
    seconds = duration % 60;

    std::printf("%i dia(s)\n", days);
    std::printf("%i hora(s)\n", hours);
    std::printf("%i minuto(s)\n", minutes);
    std::printf("%i segundo(s)\n", seconds);
}