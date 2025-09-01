#include <iostream>
#include <cctype>
#include <algorithm>
#include <string>

int main() {
    // Subfilo = Vertebrados e Invertebrados
    // Tipo = Ave, Mamifero, Inseto ou Anelideo
    // Ordem = Carnivoro, Onivoro, Herbivoro e Hematofago
    std::string subfilo, tipo, ordem;
    std::cin >> subfilo >> tipo >> ordem;

    // Validação de strings para lowercase
    std::transform(subfilo.begin(), subfilo.end(), subfilo.begin(), ::tolower);
    std::transform(tipo.begin(), tipo.end(), tipo.begin(), ::tolower);
    std::transform(ordem.begin(), ordem.end(), ordem.begin(), ::tolower);

    if (subfilo == "vertebrado") {
        if (tipo == "ave") {
            if (ordem == "carnivoro") {
                std::cout << "aguia" << std::endl;
            } else {
                std::cout << "pomba" << std::endl;
            }
        } else {
            if (ordem == "onivoro") {
                std::cout << "homem" << std::endl;
            } else {
                std::cout << "vaca" << std::endl;
            }
        }
    } else {
        if (tipo == "inseto") {
            if (ordem == "hematofago") {
                std::cout << "pulga" << std::endl;
            } else {
                std::cout << "lagarta" << std::endl;
            }
        } else {
            if (ordem == "hematofago") {
                std::cout << "sanguessuga" << std::endl;
            } else {
                std::cout << "minhoca" << std::endl;
            }
        }
    }
}