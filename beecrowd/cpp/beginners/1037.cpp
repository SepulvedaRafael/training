#include <iostream>

int main() {
    double interval;
    std::cin >> interval;

    if (interval >= 0 && interval <= 25) {
        std::cout << "Intervalo [0,25]" << std::endl;
    } else if (interval > 25 && interval <= 50) {
        std::cout << "Intervalo (25,50]" << std::endl;
    } else if (interval > 50 && interval <= 75) {
        std::cout << "Intervalo (50,75]" << std::endl;
    } else if (interval > 75 && interval <= 100){
        std::cout << "Intervalo (75,100]" << std::endl;
    } else {
        std::cout << "Fora de intervalo" << std::endl;
    }
}