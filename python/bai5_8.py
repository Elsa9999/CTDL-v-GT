def is_operator(c):
    return c in {'+', '-', '*', '/', '^'}

def prefix_to_postfix(prefix):
    stack = []  # Stack dùng để lưu các toán hạng
    
    # Đảo ngược chuỗi prefix để duyệt từ phải sang trái
    prefix = prefix[::-1]
    
    for c in prefix:
        if c.isalnum():  # Nếu là toán hạng (chữ hoặc số)
            stack.append(c)
        elif is_operator(c):  # Nếu là toán tử
            if len(stack) < 2:
                return "Invalid Expression"
            
            operand1 = stack.pop()
            operand2 = stack.pop()
            postfix_expression = operand1 + operand2 + c
            stack.append(postfix_expression)
    
    return stack[0] if len(stack) == 1 else "Invalid Expression"

if __name__ == "__main__":
    t = int(input())  # Số lượng test cases
    for _ in range(t):
        prefix_expression = input().strip()
        print(prefix_to_postfix(prefix_expression))
