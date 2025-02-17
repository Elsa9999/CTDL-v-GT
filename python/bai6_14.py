def generate_loc_phat(n, current_num, locphat_numbers):
    if len(current_num) > n:
        return

    if current_num:
        locphat_numbers.append(current_num)

    generate_loc_phat(n, current_num + "6", locphat_numbers)
    generate_loc_phat(n, current_num + "8", locphat_numbers)

def compare_decreasing(a, b):
    return a > b

for _ in range(int(input())):
    n = int(input())

    locphat_numbers_14 = []
    for i in range(1, n + 1):
        generate_loc_phat(i, "", locphat_numbers_14)

    locphat_numbers_14.sort(key=lambda x: x, reverse=True)  # Sắp xếp giảm dần

    print(len(locphat_numbers_14))
    print(*locphat_numbers_14)  # In các số lộc phát giảm dần, cách nhau bởi khoảng trắng