#include <iostream>
#include <vector>

int main() {
    int num1, num2, num3, num4, num5;
    std::cin >> num1 >> num2 >> num3 >> num4 >> num5;
    std::vector<int> nums = {num1, num2, num3, num4, num5};

    int pares = 0;
    int impares = 0;
    int positivos = 0;
    int negativos = 0;
    for (int num : nums) {
        (num % 2 == 0) ? pares++ : impares++;

        if (num > 0) {
            positivos++;
        }

        if (num < 0) {
            negativos++;
        }
    }

    std::printf("%i valor(es) par(es)\n", pares);
    std::printf("%i valor(es) impar(es)\n", impares);
    std::printf("%i valor(es) positivo(s)\n", positivos);
    std::printf("%i valor(es) negativo(s)\n", negativos);
}