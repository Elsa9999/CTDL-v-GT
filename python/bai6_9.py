def di_chuyen_tranh_vat_can(n, board, start_x, start_y, end_x, end_y):
    if board[start_x][start_y] == 'X' or board[end_x][end_y] == 'X':
        return -1  # Nếu điểm bắt đầu hoặc điểm đích là vật cản, không có đường đi

    q = [(start_x, start_y, 0)]  # Queue để thực hiện tìm kiếm theo chiều rộng (BFS)
    visited = {(start_x, start_y)}  # Set để theo dõi các ô đã посещённые

    dx = [0, 0, 1, -1]  # Mảng dx cho 4 hướng di chuyển (ngang, dọc)
    dy = [1, -1, 0, 0]  # Mảng dy cho 4 hướng di chuyển (ngang, dọc)

    while q:  # Vòng lặp BFS cho đến khi queue rỗng
        x, y, steps = q.pop(0)  # Lấy trạng thái hiện tại từ đầu queue

        if x == end_x and y == end_y:  # Nếu đã đến điểm đích, trả về số bước
            return steps

        # Duyệt qua 4 hướng di chuyển (lên, xuống, trái, phải)
        for i in range(4):
            next_x = x  # Khởi tạo tọa độ x mới
            next_y = y  # Khởi tạo tọa độ y mới

            while True:  # Di chuyển theo hướng i cho đến khi gặp vật cản hoặc biên bảng
                next_x += dx[i]  # Cập nhật tọa độ x theo hướng i
                next_y += dy[i]  # Cập nhật tọa độ y theo hướng i

                # Kiểm tra xem ô mới có hợp lệ không: nằm trong bảng và không phải vật cản
                if 0 <= next_x < n and 0 <= next_y < n and board[next_x][next_y] != 'X':
                    if (next_x, next_y) not in visited:  # Nếu ô mới chưa được посещённые
                        visited.add((next_x, next_y))  # Đánh dấu ô mới là đã посещённые
                        q.append((next_x, next_y, steps + 1))  # Thêm ô mới vào queue với số bước tăng lên 1
                else:
                    break  # Dừng di chuyển theo hướng này nếu gặp vật cản, biên bảng hoặc đã посещённые

    return -1  # Nếu không tìm thấy đường đi (trường hợp này, theo đề bài thì sẽ luôn tìm thấy nếu điểm đích không phải vật cản)


if __name__ == "__main__":
    t = int(input())  # Đọc số bộ test

    while t > 0:  # Vòng lặp cho từng bộ test
        n = int(input())  # Đọc kích thước bảng N x N
        board = []  # Khởi tạo bảng

        # Đọc bảng theo dòng:
        for _ in range(n):
            row = input()  # Đọc cả dòng vào string 'row'
            board.append(list(row))  # Chuyển string 'row' thành list các ký tự và thêm vào board

        # In bảng vừa đọc (THÊM ĐOẠN CODE NÀY):
        print("Bang da doc:")
        for row in board:
            print("".join(row))  # In các ký tự trong list 'row' liền nhau
        print("Ket thuc in bang")

        start_x, start_y, end_x, end_y = map(int, input().split())  # Đọc tọa độ điểm xuất phát và điểm đích
        start_x -= 1
        start_y -= 1
        end_x -= 1
        end_y -= 1  # Chuyển tọa độ về 0-based index

        print(di_chuyen_tranh_vat_can(n, board, start_x, start_y, end_x, end_y))  # Gọi hàm và in kết quả

        t -= 1  # Giảm bộ test