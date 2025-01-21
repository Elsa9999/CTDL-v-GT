#include <iostream>
#include <chrono>
#include <vector>

using namespace std;
using namespace std::chrono;

int find_first_element(const vector<int>& arr, int target) {
    if (arr[0] == target) {
        return 0;
    }
    return -1;
}

int main() {
    vector<int> arr = {10, 20, 30, 40, 50};

    auto start = high_resolution_clock::now();  // Bắt đầu đo thời gian

    cout << find_first_element(arr, 10) << endl;  // Output: 0

    auto end = high_resolution_clock::now();  // Kết thúc đo thời gian
    auto duration = duration_cast<milliseconds>(end - start).count();  // Thời gian thực thi (ms)

    cout << "Thời gian (ms) = " << duration << endl;

    return 0;
}
