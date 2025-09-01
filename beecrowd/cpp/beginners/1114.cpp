#include <iostream>

int main() {
    while (true) {
        int senha;
        std::cin >> senha;

        if (senha == 2002) {
            std::printf("Acesso Permitido\n");
            break;
        }

        std::printf("Senha Invalida\n");
    }
}