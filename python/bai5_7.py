def is_operator(c):
    return c in ['+', '-', '*', '/']

def prefix_to_infix(prefix):
    operands = []  # Stack để lưu trữ toán hạng

    # Duyệt biểu thức tiền tố từ phải sang trái
    prefix = prefix[::-1]  # Đảo ngược chuỗi

    for c in prefix:
        if c.isalnum():  # Kiểm tra xem ký tự có phải là toán hạng không
            operands.append(c)  # Đẩy toán hạng vào stack
        elif is_operator(c):  # Nếu ký tự là toán tử
            # Chú ý thứ tự pop: operand1 (phải) rồi operand2 (trái)
            operand1 = operands.pop()
            operand2 = operands.pop()

            # Tạo biểu thức trung tố: (operand2 operator operand1)
            infix_expression = "(" + operand2 + c + operand1 + ")"
            operands.append(infix_expression)  # Đẩy vào stack

    return operands[-1]  # Biểu thức trung tố cuối cùng trên đỉnh stack

if __name__ == "__main__":
    t = int(input())  # Đọc số test case
    for _ in range(t):
        prefix_expression = input()  # Đọc biểu thức tiền tố
        infix_expression = prefix_to_infix(prefix_expression)  # Chuyển đổi
        print(infix_expression)  # In kết quả