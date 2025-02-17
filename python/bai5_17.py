def is_correct_bracket_sequence(s):
    st = []  # Sử dụng list như stack

    for c in s:
        if c == '(':
            st.append(c)  # push vào stack
        elif c == ')':
            if not st:  # stack rỗng
                return False
            st.pop()  # pop khỏi stack

    return not st  # True nếu stack rỗng, ngược lại False


def find_longest_correct_bracket_sequence(s):
    n = len(s)
    max_len = 0

    for i in range(n):
        for j in range(i, n):
            sub = s[i:j + 1]  # Lấy chuỗi con
            if is_correct_bracket_sequence(sub):
                max_len = max(max_len, len(sub))

    return max_len


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        print(find_longest_correct_bracket_sequence(s))