#include <iostream>
#include <iomanip>

int main() {
    int codPc1, codPc2, numPc1, numPc2;
    double unitValuePc1, unitValuePc2;
    std::cin >> codPc1 >> numPc1 >> unitValuePc1;
    std::cin >> codPc2 >> numPc2 >> unitValuePc2;
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "VALOR A PAGAR: R$ " << (numPc1 * unitValuePc1) + (numPc2 * unitValuePc2) << std::endl;
}