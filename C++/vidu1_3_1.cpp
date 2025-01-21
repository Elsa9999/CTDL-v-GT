#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

void printNumbers(int n) {
    for (int i = 1; i <= n; i++) {
        cout << i << " ";
    }
    cout << endl;
}

int main() {
    int n = 5;

    auto start = high_resolution_clock::now(); // Bắt đầu đo thời gian

    printNumbers(n); // Chạy thuật toán

    auto end = high_resolution_clock::now(); // Kết thúc đo thời gian
    auto duration = duration_cast<milliseconds>(end - start).count();

    cout << "Thời gian (ms) = " << duration << endl;

    return 0;
}
