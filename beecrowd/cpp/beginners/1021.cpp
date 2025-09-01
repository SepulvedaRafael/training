#include <iostream>
#include <cmath>

int main()
{
    double n, valor, resto;
    std::cin >> n;

    std::cout << "NOTAS:" << std::endl;
    valor = n / 100;
    resto = std::fmod(n, 100);
    std::cout << (int)valor << " nota(s) de R$ 100.00" << std::endl;

    valor = resto / 50;
    resto = std::fmod(resto, 50);
    std::cout << (int)valor << " nota(s) de R$ 50.00" << std::endl;

    valor = resto / 20;
    resto = std::fmod(resto, 20);
    std::cout << (int)valor << " nota(s) de R$ 20.00" << std::endl;

    valor = resto / 10;
    resto = std::fmod(resto, 10);
    std::cout << (int)valor << " nota(s) de R$ 10.00" << std::endl;

    valor = resto / 5;
    resto = std::fmod(resto, 5);
    std::cout << (int)valor << " nota(s) de R$ 5.00" << std::endl;

    valor = resto / 2;
    resto = std::fmod(resto, 2);
    std::cout << (int)valor << " nota(s) de R$ 2.00" << std::endl;

    std::cout << "MOEDAS:" << std::endl;
    valor = resto / 1;
    resto = std::fmod(resto, 1);
    std::cout << (int)valor << " moeda(s) de R$ 1.00" << std::endl;

    valor = resto / 0.5;
    resto = std::fmod(resto, 0.5);
    std::cout << (int)valor << " moeda(s) de R$ 0.50" << std::endl;

    valor = resto / 0.25;
    resto = std::fmod(resto, 0.25);
    std::cout << (int)valor << " moeda(s) de R$ 0.25" << std::endl;

    valor = resto / 0.10;
    resto = std::fmod(resto, 0.10);
    std::cout << (int)valor << " moeda(s) de R$ 0.10" << std::endl;

    valor = resto / 0.05;
    resto = std::fmod(resto, 0.05);
    std::cout << (int)valor << " moeda(s) de R$ 0.05" << std::endl;

    valor = std::round(resto / 0.01);
    std::cout << (int)valor << " moeda(s) de R$ 0.01" << std::endl;
}
