from collections import deque

def solve():
    start_pos, end_pos = input().split()

    # Chuyển đổi ký hiệu cờ vua sang tọa độ (row, col) 0-based
    start_col = ord(start_pos[0]) - ord('a')
    start_row = int(start_pos[1]) - 1
    end_col = ord(end_pos[0]) - ord('a')
    end_row = int(end_pos[1]) - 1

    if start_col == end_col and start_row == end_row:
        return 0  # Nếu vị trí bắt đầu và kết thúc giống nhau, số bước là 0

    # Các bước di chuyển của quân mã (8 hướng)
    dx = [1, 1, 2, 2, -1, -1, -2, -2]
    dy = [2, -2, 1, -1, 2, -2, 1, -1]

    q = deque()  # Queue cho BFS: {col, row}
    dist = [[-1] * 8 for _ in range(8)]  # Ma trận khoảng cách, -1 là chưa thăm

    q.append((start_col, start_row))
    dist[start_row][start_col] = 0  # Khoảng cách từ điểm bắt đầu đến chính nó là 0

    while q:
        col, row = q.popleft()

        if col == end_col and row == end_row:
            return dist[end_row][end_col]  # Đã đến đích, trả về khoảng cách

        for i in range(8):
            next_col = col + dx[i]
            next_row = row + dy[i]

            # Kiểm tra xem vị trí mới có hợp lệ và chưa được thăm
            if 0 <= next_col < 8 and 0 <= next_row < 8 and dist[next_row][next_col] == -1:
                dist[next_row][next_col] = dist[row][col] + 1  # Cập nhật khoảng cách
                q.append((next_col, next_row))  # Thêm vào queue để duyệt tiếp

    return -1  # Không tìm thấy đường đi (trên lý thuyết không xảy ra với quân mã trên bàn cờ)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(solve())