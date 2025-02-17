from collections import deque

def solve():
    num_test_cases = int(input())

    for _ in range(num_test_cases):
        r, c = map(int, input().split())

        grid = []
        seedling_queue = deque()
        days = [[-1] * c for _ in range(r)]  # Khởi tạo ma trận days

        # Đọc input và khởi tạo
        for i in range(r):
            row = list(map(int, input().split()))
            grid.append(row)
            for j in range(c):
                if row[j] == 0:
                    seedling_queue.append((i, j))
                    days[i][j] = 0

        max_days = 0
        dr = [-1, 1, 0, 0]  # Các hướng di chuyển
        dc = [0, 0, -1, 1]

        while seedling_queue:
            current_seedling = seedling_queue.popleft()
            row = current_seedling[0]
            col = current_seedling[1]

            max_days = max(max_days, days[row][col])  # Cập nhật số ngày tối đa

            # Lan truyền dinh dưỡng
            for i in range(4):
                next_row = row + dr[i]
                next_col = col + dc[i]

                if 0 <= next_row < r and 0 <= next_col < c and grid[next_row][next_col] == 1 and days[next_row][next_col] == -1:
                    grid[next_row][next_col] = 0  # Nảy mầm
                    days[next_row][next_col] = days[row][col] + 1  # Ghi nhận ngày
                    seedling_queue.append((next_row, next_col))  # Thêm vào queue

        # Kiểm tra tất cả đã nảy mầm chưa
        all_germinated = True
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    all_germinated = False
                    break
            if not all_germinated:
                break

        if all_germinated:
            print(max_days)
        else:
            print(-1)

solve()