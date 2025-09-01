#include <iostream>

int main() {
    int n, valor, resto;
    std::cin >> n;
    std::cout << n << std::endl;

    valor = n / 100;
    resto = n % 100;
    std::cout << valor << " nota(s) de R$ 100,00" << std::endl;

    valor = resto / 50;
    resto = resto % 50;
    std::cout << valor << " nota(s) de R$ 50,00" << std::endl;

    valor = resto / 20;
    resto = resto % 20;
    std::cout << valor << " nota(s) de R$ 20,00" << std::endl;

    valor = resto / 10;
    resto = resto % 10;
    std::cout << valor << " nota(s) de R$ 10,00" << std::endl;

    valor = resto / 5;
    resto = resto % 5;
    std::cout << valor << " nota(s) de R$ 5,00" << std::endl;

    valor = resto / 2;
    resto = resto % 2;
    std::cout << valor << " nota(s) de R$ 2,00" << std::endl;

    valor = resto / 1;
    resto = resto % 1;
    std::cout << valor << " nota(s) de R$ 1,00" << std::endl;
}