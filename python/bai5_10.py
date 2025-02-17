def is_operator(c):
    return c in {'+', '-', '*', '/', '^'}

def postfix_to_infix(postfix):
    stack = []
    
    for c in postfix:
        if c.isalnum():  # Nếu là toán hạng (chữ hoặc số), đẩy vào stack
            stack.append(c)
        elif is_operator(c):  # Nếu là toán tử
            if len(stack) < 2:
                return "Invalid Expression"
            
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            infix_expression = f"({operand1}{c}{operand2})"
            stack.append(infix_expression)
    
    return stack[0] if len(stack) == 1 else "Invalid Expression"

if __name__ == "__main__":
    t = int(input())  # Đọc số lượng bộ test
    input()  # Bỏ qua ký tự newline sau số nguyên
    
    for _ in range(t):
        postfix_expression = input().strip()
        infix_expression = postfix_to_infix(postfix_expression)
        print(infix_expression)
