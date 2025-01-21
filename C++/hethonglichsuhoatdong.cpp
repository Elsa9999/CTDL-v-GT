#include <iostream>
#include <stack>
#include <unordered_map>
#include <string>

class Robot {
private:
    std::stack<std::string> history; // Sử dụng stack làm ngăn xếp lưu lịch sử hoạt động
    std::unordered_map<std::string, std::string> directions = {
        {"tiến lên", "lùi lại"},
        {"lùi lại", "tiến lên"},
        {"quay trái", "quay phải"},
        {"quay phải", "quay trái"}
    };

public:
    void executeCommand(const std::string& command) {
        // Thực hiện lệnh di chuyển và lưu vào lịch sử
        std::cout << "Robot thực hiện lệnh: " << command << std::endl;
        history.push(command);
    }

    void undo() {
        // Hoàn tác lệnh di chuyển cuối cùng
        if (history.empty()) {
            std::cout << "Không có lệnh nào để hoàn tác." << std::endl;
            return;
        }

        std::string lastCommand = history.top();
        history.pop();
        
        if (directions.find(lastCommand) != directions.end()) {
            std::string reverseCommand = directions[lastCommand];
            std::cout << "Hoàn tác lệnh: " << lastCommand << " -> Thực hiện: " << reverseCommand << std::endl;
        } else {
            std::cout << "Không tìm thấy lệnh đảo ngược cho: " << lastCommand << std::endl;
        }
    }

    void printHistory() {
        if (history.empty()) {
            std::cout << "Lịch sử hoạt động trống." << std::endl;
            return;
        }

        std::cout << "Lịch sử hoạt động của Robot (mới nhất đầu tiên):" << std::endl;
        
        // Tạm thời lưu lịch sử vào stack phụ để duyệt ngược
        std::stack<std::string> tempHistory = history;
        while (!tempHistory.empty()) {
            std::cout << tempHistory.top() << std::endl;
            tempHistory.pop();
        }
    }
};

int main() {
    Robot robot;

    robot.executeCommand("tiến lên");
    robot.executeCommand("quay trái");
    robot.executeCommand("tiến lên");
    robot.executeCommand("lùi lại");

    robot.printHistory();

    robot.undo();
    robot.undo();
    robot.undo();
    robot.undo();
    robot.undo();

    robot.printHistory();

    return 0;
}
