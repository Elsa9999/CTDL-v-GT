def evaluate_postfix(postfix):
    values = []

    for c in postfix:
        if c.isdigit():
            values.append(int(c))  # Chuyển ký tự số sang số nguyên
        else:
            if len(values) < 2:
                return -99999  # Biểu thức không hợp lệ
            val2 = values.pop()
            val1 = values.pop()

            if c == '+':
                values.append(val1 + val2)
            elif c == '-':
                values.append(val1 - val2)
            elif c == '*':
                values.append(val1 * val2)
            elif c == '/':
                if val2 == 0:  # Kiểm tra chia cho 0
                    return -99999
                values.append(int(val1 / val2)) # Chia lấy phần nguyên
            # Có thể thêm các toán tử khác (ví dụ: ^) vào đây

    if len(values) == 1:
        return values[-1]
    else:
        return -99999  # Biểu thức không hợp lệ

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        postfix_expression = input()
        result = evaluate_postfix(postfix_expression)
        print(result)