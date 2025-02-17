def decode_string(s):
    counts = []  # Sử dụng list như stack cho counts
    strs = []    # Sử dụng list như stack cho strs
    res = ""

    i = 0
    while i < len(s):
        if s[i].isdigit():
            count = 0
            while i < len(s) and s[i].isdigit():
                count = count * 10 + int(s[i])
                i += 1
            i -= 1  # Điều chỉnh i sau khi đọc số
            counts.append(count)
        elif s[i] == '[':
            strs.append(res)
            res = ""
        elif s[i] == ']':
            prev_str = strs.pop()
            repeat_count = counts.pop()
            temp_str = ""
            for _ in range(repeat_count):
                temp_str += res
            res = prev_str + temp_str
        else:
            res += s[i]
        i += 1
    return res

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        encoded_str = input()
        print(decode_string(encoded_str))