#include <iostream>

int main()
{
    int N;
    std::cin >> N;
    for (int i = 0; i < N/2+1; i++){
        for (int j = 0; j < N; j++){
            if ((i <= j) & (j < N-i)){
                std::cout << '*';
            } else {
                std::cout << ' ';
            }
        }
        std::cout << '\n';
    }
    return 0;
}
