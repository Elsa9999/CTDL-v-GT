def is_valid(n):
    s = str(n)  # Bước 1: Chuyển số thành chuỗi
    digits = set()  # Bước 2: Khởi tạo set theo dõi chữ số

    for c in s:  # Bước 3: Duyệt từng chữ số
        if c > '5':  # Kiểm tra Điều kiện 2
            return False
        if c in digits:  # Kiểm tra Điều kiện 1 (Python set hỗ trợ kiểm tra trực tiếp)
            return False
        digits.add(c)  # Thêm chữ số vào set

    return True  # Bước 4: Trả về True nếu hợp lệ

if __name__ == "__main__":
    t = int(input())  # Biến t để lưu số lượng test cases

    while t > 0:  # Vòng lặp test cases (có thể dùng for _ in range(t):)
        l, r = map(int, input().split())  # Đọc L và R cùng lúc, chuyển thành số nguyên

        count = 0  # Khởi tạo biến đếm
        for i in range(l, r + 1):  # Vòng lặp duyệt khoảng [L, R] (range trong Python cần +1 ở cuối)
            if is_valid(i):  # Kiểm tra số hợp lệ
                count += 1  # Tăng biến đếm

        print(count)  # In kết quả
        t -= 1  # Giảm biến đếm test cases (hoặc dùng for loop)