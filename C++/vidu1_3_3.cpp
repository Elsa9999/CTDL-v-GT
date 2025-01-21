#include <iostream>
#include <chrono>
#include <vector>

using namespace std;
using namespace std::chrono;

int binary_search(const vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};

    auto start = high_resolution_clock::now();  // Bắt đầu đo thời gian

    cout << binary_search(arr, 10) << endl;  // Output: 9

    auto end = high_resolution_clock::now();  // Kết thúc đo thời gian
    auto duration = duration_cast<milliseconds>(end - start).count();  // Thời gian thực thi (ms)

    cout << "Thời gian (ms) = " << duration << endl;

    return 0;
}
