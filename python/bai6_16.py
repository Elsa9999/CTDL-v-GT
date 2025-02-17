from collections import deque

def solve():
    m, n = map(int, input().split())
    a = [[0] * (n + 1) for _ in range(m + 1)]  # Khởi tạo ma trận A

    for i in range(1, m + 1):
        row = list(map(int, input().split()))
        for j in range(1, n + 1):
            a[i][j] = row[j - 1] #chú ý chỗ này

    q = deque()
    visited = [[False] * (n + 1) for _ in range(m + 1)]

    q.append((1, 1, 0))
    visited[1][1] = True

    while q:
        row, col, steps = q.popleft()

        if row == m and col == n:
            return steps

        next_row_down1 = row + 1
        next_row_down_val = row + a[row][col]
        next_col = col

        # Di chuyển xuống 1 đơn vị
        if next_row_down1 <= m and not visited[next_row_down1][next_col]:
            visited[next_row_down1][next_col] = True
            q.append((next_row_down1, next_col, steps + 1))

        # Di chuyển xuống theo giá trị A[i][j]
        if next_row_down_val <= m and not visited[next_row_down_val][next_col]:
            visited[next_row_down_val][next_col] = True
            q.append((next_row_down_val, next_col, steps + 1))

    return -1

t = int(input())
for _ in range(t):
    print(solve())