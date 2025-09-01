#include <iostream>
#include <cmath>

int main() {
    for (int step = 0; step <= 10; ++step) {
        double i = step * 0.2;
        double j = 1.0 + step * 0.2;
        for (int k = 0; k < 3; ++k) {
            double jj = j + k;
            if (std::fabs(i - std::round(i)) < 1e-9) {
                std::printf("I=%d J=%d\n", (int)std::round(i), (int)jj);
            } else {
                std::printf("I=%.1f J=%.1f\n", i, jj);
            }
        }
    }
}
