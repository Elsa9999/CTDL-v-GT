from collections import deque

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve():
    start_prime, end_prime = map(int, input().split())

    if start_prime == end_prime:
        return 0

    prime_numbers = set()
    for i in range(1000, 10000):
        if is_prime(i):
            prime_numbers.add(i)

    if start_prime not in prime_numbers or end_prime not in prime_numbers:
        return -1

    q = deque()
    q.append((start_prime, 0))  # (current_prime, steps)
    visited = {start_prime}

    while q:
        u, steps = q.popleft()

        if u == end_prime:
            return steps

        s = str(u)
        for i in range(4):
            for digit in range(10):  # Iterate through digits 0-9
                temp = list(s) # Convert string to list for mutability
                temp[i] = str(digit)
                v = int("".join(temp)) # Join back to string and convert to int

                if 1000 <= v <= 9999 and v in prime_numbers and v not in visited:
                    visited.add(v)
                    q.append((v, steps + 1))

    return -1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(solve())