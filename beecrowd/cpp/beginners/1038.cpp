#include <iostream>

int main() {
    double code, quantit;
    std::cin >> code >> quantit;

    switch ((int)code) {
        case 1:
            std::printf("Total: R$ %.2f\n", quantit * 4);
            break;
        case 2:
            std::printf("Total: R$ %.2f\n", quantit * 4.5);
            break;
        case 3:
            std::printf("Total: R$ %.2f\n", quantit * 5);
            break;
        case 4:
            std::printf("Total: R$ %.2f\n", quantit * 2);
            break;
        case 5:
            std::printf("Total: R$ %.2f\n", quantit * 1.5);
            break;
    }
}