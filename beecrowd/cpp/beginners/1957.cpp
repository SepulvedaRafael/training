#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>

int main() {
    int v;
    std::cin >> v;

    std::stringstream stream;
    stream << std::hex << v;
    std::string result(stream.str());
    std::transform(result.begin(), result.end(), result.begin(), ::toupper);
    std::cout << result << std::endl;
}