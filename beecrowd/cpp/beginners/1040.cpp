#include <iostream>

int main() {
    double n1, n2, n3, n4, media, mediaExame, nExame;
    std::cin >> n1 >> n2 >> n3 >> n4;

    media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10;
    std::printf("Media: %.1f\n", media);

    if (media >= 7.0) {
        std::cout << "Aluno aprovado." << std::endl;
    } else if (media >= 5.0 && media < 7) {
        std::cout << "Aluno em exame." << std::endl;
        std::cin >> nExame;
        std::printf("Nota do exame: %.1f\n", nExame);
        mediaExame = (media + nExame) / 2;

        if (mediaExame >= 5.0) {
            std::cout << "Aluno aprovado." << std::endl;
        } else if (mediaExame < 5) {
            std::cout << "Aluno reprovado." << std::endl;
        }

        std::printf("Media final: %.1f\n", mediaExame);
    } else {
        std::cout << "Aluno reprovado." << std::endl;
    }
}