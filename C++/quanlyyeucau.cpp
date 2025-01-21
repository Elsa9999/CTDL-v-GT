#include <iostream>
#include <stack>
#include <string>
#include <vector> // Thêm thư viện vector

class UndoRedoManager {
private:
    std::stack<std::string> undoStack; // Ngăn xếp lưu các hành động đã thực hiện
    std::stack<std::string> redoStack; // Ngăn xếp lưu các hành động hoàn tác

public:
    void doAction(const std::string& action) {
        // Thực hiện một hành động và thêm vào undo stack
        undoStack.push(action);
        while (!redoStack.empty()) {
            redoStack.pop(); // Xóa redo stack khi có hành động mới
        }
        std::cout << "Thực hiện hành động: " << action << std::endl;
        printStacks();
    }

    void undo() {
        // Hoàn tác hành động cuối cùng
        if (undoStack.empty()) {
            std::cout << "Không có hành động nào để hoàn tác." << std::endl;
            printStacks();
            return;
        }

        std::string action = undoStack.top();
        undoStack.pop();
        redoStack.push(action);
        std::cout << "Hoàn tác hành động: " << action << std::endl;
        printStacks();
    }

    void redo() {
        // Làm lại hành động đã hoàn tác
        if (redoStack.empty()) {
            std::cout << "Không có hành động nào để làm lại." << std::endl;
            printStacks();
            return;
        }

        std::string action = redoStack.top();
        redoStack.pop();
        undoStack.push(action);
        std::cout << "Làm lại hành động: " << action << std::endl;
        printStacks();
    }

    void printStacks() {
        // In trạng thái của undo và redo stack
        std::cout << "  undoStack: [";
        printStack(undoStack);
        std::cout << "]\n  redoStack: [";
        printStack(redoStack);
        std::cout << "]\n" << std::endl;
    }

private:
    void printStack(std::stack<std::string> stack) {
        // In các phần tử trong ngăn xếp (tạm thời sử dụng bản sao)
        std::vector<std::string> elements;
        while (!stack.empty()) {
            elements.push_back(stack.top());
            stack.pop();
        }
        for (auto it = elements.rbegin(); it != elements.rend(); ++it) {
            std::cout << *it << (it + 1 != elements.rend() ? ", " : "");
        }
    }
};

int main() {
    UndoRedoManager manager;

    manager.doAction("Gõ 'Hello'");  // Hành động 1
    manager.doAction("Gõ ' World'"); // Hành động 2
    manager.undo();                      // Hành động 3
    manager.undo();                      // Hành động 4
    manager.redo();                      // Hành động 5
    manager.redo();
    manager.undo();
    manager.doAction("Gõ '!'"); 
    manager.undo();
    manager.undo();
    manager.redo();

    return 0;
}
