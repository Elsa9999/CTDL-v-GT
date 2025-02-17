def find_smallest_number(s):
    n = len(s) + 1
    result = ""
    used = [False] * 10  # Mảng đánh dấu số đã dùng

    def solve(current_digit_index):
        if current_digit_index == n:
            return True

        for digit in range(1, 10):
            if not used[digit]:
                if current_digit_index > 0:
                    if s[current_digit_index - 1] == 'I' and int(result[current_digit_index - 1]) >= digit:
                        continue
                    if s[current_digit_index - 1] == 'D' and int(result[current_digit_index - 1]) <= digit:
                        continue

                used[digit] = True
                result += str(digit)

                if solve(current_digit_index + 1):
                    return True

                used[digit] = False  # Backtracking
                result = result[:-1]  # Remove last char

        return False

    solve(0)
    return result

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        print(find_smallest_number(s))