#include <iostream>

int main() {
    int qtd_produtos;
    std::cin >> qtd_produtos;

    double total = 0;
    for (int i = 0; i < qtd_produtos; i++) {
        int codigo, qtd_produto;
        std::cin >> codigo >> qtd_produto;

        switch (codigo) {
            case 1001:
                total += qtd_produto * 1.5;
                break;
            case 1002:
                total += qtd_produto * 2.5;
                break;
            case 1003:
                total += qtd_produto * 3.5;
                break;
            case 1004:
                total += qtd_produto * 4.5;
                break;
            case 1005:
                total += qtd_produto * 5.5;
                break;
        }
    }

    std::printf("%.2f\n", total);
}