#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

void printPairs(int n) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cout << "(" << i << ", " << j << ") ";
        }
    }
    cout << endl;
}

int main() {
    int n = 3; // Số lượng phần tử

    auto start = high_resolution_clock::now(); // Bắt đầu đo thời gian

    printPairs(n); // Chạy thuật toán

    auto end = high_resolution_clock::now(); // Kết thúc đo thời gian
    auto duration = duration_cast<milliseconds>(end - start).count(); // Thời gian thực thi (ms)

    cout << "Thời gian (ms) = " << duration << endl;

    return 0;
}
