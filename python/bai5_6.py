def precedence(op):
    """Xác định độ ưu tiên của toán tử."""
    if op == '^':
        return 3  # Lũy thừa có độ ưu tiên cao nhất
    if op in ('*', '/'):
        return 2  # Nhân, chia có độ ưu tiên trung bình
    if op in ('+', '-'):
        return 1  # Cộng, trừ có độ ưu tiên thấp nhất
    return 0  # Dấu ngoặc và toán hạng có độ ưu tiên thấp nhất


def infix_to_postfix(infix):
    """Chuyển đổi biểu thức trung tố (infix) sang hậu tố (postfix)."""
    postfix = ""  # Kết quả biểu thức hậu tố
    operators = []  # Stack để lưu toán tử

    for c in infix:
        if c.isalnum():  # Nếu là toán hạng (chữ hoặc số), thêm trực tiếp vào hậu tố
            postfix += c
        elif c == '(':  # Nếu là dấu ngoặc mở, đẩy vào stack
            operators.append(c)
        elif c == ')':  # Nếu là dấu ngoặc đóng, lấy toán tử từ stack cho đến khi gặp '('
            while operators and operators[-1] != '(':
                postfix += operators.pop()
            operators.pop()  # Loại bỏ '(' khỏi stack
        else:  # Nếu là toán tử (+, -, *, /, ^)
            while operators and precedence(operators[-1]) >= precedence(c):
                postfix += operators.pop()  # Lấy toán tử có độ ưu tiên cao hơn ra khỏi stack
            operators.append(c)  # Đẩy toán tử hiện tại vào stack

    # Lấy hết toán tử còn lại trong stack
    while operators:
        postfix += operators.pop()

    return postfix


if __name__ == "__main__":
    t = int(input())  # Đọc số lượng test case
    for _ in range(t):
        infix_expression = input().strip()  # Đọc biểu thức trung tố từ input
        print(infix_to_postfix(infix_expression))  # Chuyển đổi và in ra hậu tố
