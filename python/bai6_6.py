from collections import deque
import math

def bien_doi_so_tu_nhien(n):
    if n == 1:
        return 0

    q = deque()
    visited = set()

    q.append((n, 0))
    visited.add(n)

    while q:
        current_n, steps = q.popleft()

        # Thao tác (a): N = N - 1
        subtract_n = current_n - 1
        if subtract_n >= 1 and subtract_n not in visited:
            if subtract_n == 1:
                return steps + 1
            q.append((subtract_n, steps + 1))
            visited.add(subtract_n)

        # Thao tác (b): N = max(u, v) nếu u * v = N (u > 1, v > 1)
        if current_n > 1:
            for u in range(2, int(math.sqrt(current_n)) + 1):
                if current_n % u == 0:
                    v = current_n // u
                    max_uv = max(u, v)
                    if max_uv not in visited:
                        # if max_uv == 1:  # Không cần thiết
                        #     return steps + 1
                        q.append((max_uv, steps + 1))
                        visited.add(max_uv)

    return -1  # Không nên xảy ra

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(bien_doi_so_tu_nhien(n))