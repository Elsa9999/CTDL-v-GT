from collections import deque

def find_smallest_divisible_by_n(n):
    q = deque()  # Sử dụng deque cho queue
    visited_remainders = set()

    q.append(("9", 9 % n))
    visited_remainders.add(9 % n)

    while q:
        current_num_str, current_remainder = q.popleft()

        if current_remainder == 0:
            return current_num_str

        # Thêm '0'
        next_num_str_0 = current_num_str + "0"
        next_remainder_0 = (current_remainder * 10) % n
        if next_remainder_0 not in visited_remainders:
            visited_remainders.add(next_remainder_0)
            q.append((next_num_str_0, next_remainder_0))

        # Thêm '9'
        next_num_str_9 = current_num_str + "9"
        next_remainder_9 = (current_remainder * 10 + 9) % n
        if next_remainder_9 not in visited_remainders:
            visited_remainders.add(next_remainder_9)
            q.append((next_num_str_9, next_remainder_9))

    return ""  # Không nên xảy ra trong bài này

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(find_smallest_divisible_by_n(n))