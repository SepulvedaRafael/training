#include <iostream>
#include <map>
#include <string>

int main() {
    char tipo;
    int n, quantia;
    std::cin >> n;

    std::map<char, int> cobaias;
    for (int i = 0; i < n; i++) {
        std::cin >> quantia >> tipo;
        cobaias[tipo] += quantia;
    }

    int total = cobaias['C'] + cobaias['R'] + cobaias['S'];

    std::printf("Total: %i cobaias\n", total);
    std::printf("Total de coelhos: %i\n", cobaias['C']);
    std::printf("Total de ratos: %i\n", cobaias['R']);
    std::printf("Total de sapos: %i\n", cobaias['S']);
    std::printf("Percentual de coelhos: %.2f %%\n", (double)cobaias['C'] / total * 100);
    std::printf("Percentual de ratos: %.2f %%\n", (double)cobaias['R'] / total * 100);
    std::printf("Percentual de sapos: %.2f %%\n", (double)cobaias['S'] / total * 100);
}