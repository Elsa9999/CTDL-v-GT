def is_operator(c):
    return c in ['+', '-', '*', '/', '^']

def postfix_to_prefix(postfix):
    operands = []

    for c in postfix:
        if c.isalnum():
            operands.append(c)
        elif is_operator(c):
            if len(operands) < 2:
                return "Invalid Expression"
            operand1 = operands.pop()
            operand2 = operands.pop()
            prefix_expression = c + operand2 + operand1
            operands.append(prefix_expression)

    if len(operands) == 1:
        return operands[-1]
    else:
        return "Invalid Expression"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        postfix_expression = input()
        prefix_expression = postfix_to_prefix(postfix_expression)
        print(prefix_expression)