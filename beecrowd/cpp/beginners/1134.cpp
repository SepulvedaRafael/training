#include <iostream>

int main() {
    int alcool = 0, diesel = 0, gasolina = 0;
    bool status = true;
    while (status) {
        int tipo;
        std::cin >> tipo;

        switch (tipo) {
            case 1:
                alcool++;
                break;
            case 2:
                gasolina++;
                break;
            case 3:
                diesel++;
                break;
            case 4:
                status = false;
                break;
        }
    }

    std::cout << "MUITO OBRIGADO" << std::endl;
    std::printf("Alcool: %i\n", alcool);
    std::printf("Gasolina: %i\n", gasolina);
    std::printf("Diesel: %i\n", diesel);
}