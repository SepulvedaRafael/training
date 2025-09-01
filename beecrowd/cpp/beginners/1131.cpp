#include <iostream>

int main() {
    int jogos = 0, vitoriasInter = 0, vitoriasGre = 0, empates = 0;
    bool status = true;
    while (status) {
        int golsInter, golsGre;
        std::cin >> golsInter >> golsGre;

        if (golsInter > golsGre) {
            vitoriasInter++;
        } else if (golsInter == golsGre) {
            empates++;
        } else {
            vitoriasGre++;
        }

        jogos++;

        while (true) {
            std::cout << "Novo grenal (1-sim 2-nao)" << std::endl;
            int resp;
            std::cin >> resp;

            if (resp == 1) {
                break;
            } else if (resp == 2) {
                status = false;
                break;
            }
        }
    }

    std::printf("%i grenais\n", jogos);
    std::printf("Inter:%i\n", vitoriasInter);
    std::printf("Gremio:%i\n", vitoriasGre);
    std::printf("Empates:%i\n", empates);

    if (vitoriasInter > vitoriasGre) {
        std::printf("Inter venceu mais\n");
    } else if (vitoriasGre == vitoriasInter) {
        std::printf("Nao houve vencedor\n");
    } else {
        std::printf("Gremio venceu mais\n");
    }
}