#include <iostream>
#include <queue>
#include <string>

class RequestQueue {
private:
    std::queue<std::string> queue; // Sử dụng queue để lưu các yêu cầu

public:
    void enqueue(const std::string& request) {
        // Thêm yêu cầu vào cuối hàng đợi
        queue.push(request);
        std::cout << "\u0110\u00e3 th\u00eam y\u00eau c\u1ea7u: " << request << " v\u00e0o h\u00e0ng \u0111\u1ee3i." << std::endl;
    }

    void dequeue() {
        // Lấy và xử lý yêu cầu từ đầu hàng đợi
        if (queue.empty()) {
            std::cout << "H\u00e0ng \u0111\u1ee3i r\u1ed7ng, kh\u00f4ng c\u00f3 y\u00eau c\u1ea7u n\u00e0o \u0111\u1ec3 x\u1eed l\u00fd." << std::endl;
            return;
        }

        std::string request = queue.front();
        queue.pop();
        std::cout << "\u0110ang x\u1eed l\u00fd y\u00eau c\u1ea7u: " << request << std::endl;
    }

    bool isEmpty() {
        // Kiểm tra xem hàng đợi có rỗng không
        return queue.empty();
    }

    size_t size() {
        // Trả về kích thước hàng đợi
        return queue.size();
    }
};

int main() {
    RequestQueue requestQueue;

    // Thêm các yêu cầu vào hàng đợi
    requestQueue.enqueue("Y\u00eau c\u1ea7u A");
    requestQueue.enqueue("Y\u00eau c\u1ea7u B");
    requestQueue.enqueue("Y\u00eau c\u1ea7u C");

    std::cout << "K\u00edch th\u01b0\u1edbc h\u00e0ng \u0111\u1ee3i: " << requestQueue.size() << std::endl;

    // Xử lý các yêu cầu
    requestQueue.dequeue();
    requestQueue.dequeue();

    // Thêm yêu cầu mới
    requestQueue.enqueue("Y\u00eau c\u1ea7u D");

    // Xử lý yêu cầu tiếp theo
    requestQueue.dequeue();
    requestQueue.dequeue();
    requestQueue.dequeue();

    return 0;
}
