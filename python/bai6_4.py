from collections import deque

def find_smallest_bdn_of_n(n):
    q = deque()
    visited_remainders = set()

    q.append(("1", 1 % n))  # Khởi tạo với số 1
    visited_remainders.add(1 % n)

    while q:
        current_bdn_str, current_remainder = q.popleft()

        if current_remainder == 0:
            return current_bdn_str

        # Thêm 0 vào cuối
        next_bdn_str_0 = current_bdn_str + "0"
        next_remainder_0 = (current_remainder * 10) % n
        if next_remainder_0 not in visited_remainders:
            visited_remainders.add(next_remainder_0)
            q.append((next_bdn_str_0, next_remainder_0))

        # Thêm 1 vào cuối
        next_bdn_str_1 = current_bdn_str + "1"
        next_remainder_1 = (current_remainder * 10 + 1) % n
        if next_remainder_1 not in visited_remainders:
            visited_remainders.add(next_remainder_1)
            q.append((next_bdn_str_1, next_remainder_1))

    return ""  # Trường hợp này không nên xảy ra với giới hạn của n

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(find_smallest_bdn_of_n(n))