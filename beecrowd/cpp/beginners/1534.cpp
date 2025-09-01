#include <iostream>
#include <string>

int main() {
    std::string n_str;
    while (std::getline(std::cin, n_str)) {
        int n = std::stoi(n_str);

        for (int i = 0; i < n; ++i) {
            std::string elemento = "";
            for (int j = 0; j < n; ++j) {
                if (n % 2 == 0) {
                    if (i == j) {
                        elemento += '1';
                    } else if (i == (n - 1 - j)) {
                        elemento += '2';
                    } else {
                        elemento += '3';
                    }
                } else {
                    if (i == (n - 1 - j)) {
                        elemento += '2';
                    } else if (i == j) {
                        elemento += '1';
                    } else {
                        elemento += '3';
                    }
                }
            }
            std::cout << elemento << std::endl;
        }
    }
}
