#include <iostream>

int main() {
    int cont = 0;
    double soma = 0.0;
    bool status = true;
    while (status) {
        double nota;
        std::cin >> nota;

        if (nota < 0 || nota > 10) {
            std::cout << "nota invalida" << std::endl;
        } else {
            soma += nota;
            cont++;

            if (cont == 2) {
                std::printf("media = %.2f\n", soma / 2.0);
                int resp;
                while (true) {
                    std::cout << "novo calculo (1-sim 2-nao)" << std::endl;
                    std::cin >> resp;

                    if (resp == 1) {
                        cont = 0;
                        soma = 0.0;
                        break;
                    } else if (resp == 2) {
                        status = false;
                        break;
                    }
                }
            }
        }
    }
}