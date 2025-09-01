#include <iostream>

int main()
{
    int i = 1;
    int j = 7;
    while (i <= 9)
    {
        int diff = j - 2;
        for (; j >= diff; j--)
        {
            std::printf("I=%i J=%i\n", i, j);
        }
        i += 2;
        j += 5;
    }
}