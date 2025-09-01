#include <iostream>
#include <string>

int main() {
    int cases, x;
    std::cin >> cases;

    std::string msg = "";
    for (int i = 0; i < cases; i++) {
        std::cin >> x;

        (x % 2 == 0) ? msg = "EVEN " : msg = "ODD ";
        (x > 0) ? msg += "POSITIVE" : msg += "NEGATIVE";
        (x == 0) ? msg = "NULL" : "";
        std::cout << msg << std::endl;
    }
}