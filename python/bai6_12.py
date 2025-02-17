def generate_loc_phat(n, current_num, locphat_numbers):
    if len(current_num) > n:
        return

    if current_num:
        locphat_numbers.append(current_num)

    generate_loc_phat(n, current_num + "6", locphat_numbers)
    generate_loc_phat(n, current_num + "8", locphat_numbers)

def compare_decreasing(a, b):
    return a > b

def compare_increasing(a, b):
    return a < b

for _ in range(int(input())):
    n = int(input())

    # Bài 6.12
    locphat_numbers_12 = []
    for i in range(1, n + 1):
        generate_loc_phat(i, "", locphat_numbers_12)
    locphat_numbers_12.sort(key=lambda x: x, reverse=True) # Sắp xếp giảm dần

    print(*locphat_numbers_12) # In các số lộc phát giảm dần

    # Bài 6.13
    locphat_numbers_13 = []
    for i in range(1, n + 1):
        generate_loc_phat(i, "", locphat_numbers_13)
    locphat_numbers_13.sort() # Sắp xếp tăng dần (mặc định)

    print(len(locphat_numbers_13)) # In số lượng các số lộc phát
    print(*locphat_numbers_13) # In các số lộc phát tăng dần