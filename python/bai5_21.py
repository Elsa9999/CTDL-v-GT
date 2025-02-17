def is_correct_bracket_sequence(s):
    st = []  # Khởi tạo một stack (dùng list) để theo dõi ngoặc mở

    for c in s:  # Duyệt qua từng ký tự trong chuỗi s
        if c == '(':  # Nếu ký tự là ngoặc mở
            st.append(c)  # Đẩy ngoặc mở vào stack
        elif c == ')':  # Nếu ký tự là ngoặc đóng
            if not st:  # Kiểm tra stack có rỗng không
                return False  # Nếu rỗng, nghĩa là không có ngoặc mở tương ứng, trả về False (không đúng)
            st.pop()  # Nếu không rỗng, pop (lấy ra) một ngoặc mở từ stack (tìm thấy cặp ngoặc hợp lệ)

    return not st  # Sau khi duyệt xong chuỗi, nếu stack rỗng, nghĩa là tất cả ngoặc mở đều có ngoặc đóng tương ứng, trả về True (dãy ngoặc đúng)


if __name__ == "__main__":
    t = int(input())  # Biến t để lưu số lượng bộ test
    for _ in range(t):  # Vòng lặp chạy t lần để xử lý từng bộ test
        p = input()  # Biến p để lưu biểu thức ngoặc đầu vào
        total_length = 0  # Biến total_length để tính tổng độ dài các biểu thức con đúng, khởi tạo bằng 0
        n = len(p)  # Lấy độ dài của biểu thức p

        for i in range(n):  # Vòng lặp ngoài để chọn vị trí bắt đầu của chuỗi con (từ index 0 đến n-1)
            for j in range(i, n):  # Vòng lặp trong để chọn vị trí kết thúc của chuỗi con (từ index i đến n-1)
                sub = p[i:j+1]  # Tạo chuỗi con 'sub' từ biểu thức p, bắt đầu từ index i và kết thúc ở index j
                if len(sub) >= 2 and is_correct_bracket_sequence(sub):  # Kiểm tra 2 điều kiện:
                    # 1. Độ dài chuỗi con phải ít nhất là 2 (theo yêu cầu đề bài)
                    # 2. Chuỗi con 'sub' phải là một dãy ngoặc đúng (sử dụng hàm is_correct_bracket_sequence)
                    total_length += len(sub)  # Nếu cả hai điều kiện đều đúng, cộng độ dài của chuỗi con vào tổng độ dài

        print(total_length)  # In ra tổng độ dài của tất cả các biểu thức con viết đúng cho bộ test hiện tại