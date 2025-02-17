def precedence(op):
    if op == '*' or op == '/':
        return 2
    if op == '+' or op == '-':
        return 1
    return 0

def evaluate_infix(expression):
    values = []
    operators = []

    i = 0
    while i < len(expression):
        if expression[i].isspace():
            i += 1
            continue
        elif expression[i].isdigit():
            value = 0
            while i < len(expression) and expression[i].isdigit():
                value = (value * 10) + int(expression[i])
                i += 1
            values.append(value)
            i -= 1  # Important: Adjust index because the loop increments it
        elif expression[i] == '(':
            operators.append('(')
        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                op = operators.pop()
                val2 = values.pop()
                val1 = values.pop()
                if op == '+':
                    values.append(val1 + val2)
                elif op == '-':
                    values.append(val1 - val2)
                elif op == '*':
                    values.append(val1 * val2)
                elif op == '/':
                    values.append(int(val1 / val2))  # Integer division
            operators.pop()  # Remove '('
        else:  # Operator
            while operators and operators[-1] != '(' and precedence(operators[-1]) >= precedence(expression[i]):
                op = operators.pop()
                val2 = values.pop()
                val1 = values.pop()
                if op == '+':
                    values.append(val1 + val2)
                elif op == '-':
                    values.append(val1 - val2)
                elif op == '*':
                    values.append(val1 * val2)
                elif op == '/':
                    values.append(int(val1 / val2))  # Integer division
            operators.append(expression[i])
        i += 1

    while operators:
        op = operators.pop()
        val2 = values.pop()
        val1 = values.pop()
        if op == '+':
            values.append(val1 + val2)
        elif op == '-':
            values.append(val1 - val2)
        elif op == '*':
            values.append(val1 * val2)
        elif op == '/':
            values.append(int(val1 / val2))  # Integer division

    return values[-1]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        infix_expression = input()
        result = evaluate_infix(infix_expression)
        print(result)