def generate_loc_phat(n, current_num, locphat_numbers):
    if len(current_num) > n:
        return
    if current_num:  # Check if current_num is not empty
        locphat_numbers.append(current_num)
    generate_loc_phat(n, current_num + "6", locphat_numbers)
    generate_loc_phat(n, current_num + "8", locphat_numbers)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())

        locphat_numbers_13 = []
        for i in range(1, n + 1):
            generate_loc_phat(i, "", locphat_numbers_13)

        locphat_numbers_13.sort()  # Sort in increasing order (lexicographically)

        print(len(locphat_numbers_13))
        print(*locphat_numbers_13)  # Print the numbers separated by spaces