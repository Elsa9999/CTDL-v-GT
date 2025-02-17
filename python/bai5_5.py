def solve_expression(expression, sign_multiplier):
    output_expression = ""
    i = 0
    while i < len(expression):
        char_at_i = expression[i]
        if char_at_i.isalpha():
            output_expression += char_at_i
        elif char_at_i == '+':
            output_expression += '+' if sign_multiplier == 1 else '-'
        elif char_at_i == '-':
            output_expression += '-' if sign_multiplier == 1 else '+'
        elif char_at_i == '(':
            start_index = i
            balance = 1
            i += 1
            while balance > 0:
                if expression[i] == '(':
                    balance += 1
                elif expression[i] == ')':
                    balance -= 1
                i += 1
            end_index = i - 1
            substring_inside = expression[start_index + 1:end_index]
            inner_result = solve_expression(substring_inside, -sign_multiplier)
            output_expression += inner_result
            i -= 1
        elif char_at_i == ')':
            pass  # No need to handle ')' directly
        i += 1
    return output_expression

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        p1 = input()
        p2 = input()
        solved_p1 = solve_expression(p1, 1)
        solved_p2 = solve_expression(p2, 1)
        if solved_p1 == solved_p2:
            print("YES")
        else:
            print("NO")