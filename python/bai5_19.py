def main():
    t = int(input())  # Đọc số lượng bộ test
    
    for _ in range(t):  # Xử lý từng bộ test
        n = int(input())  # Đọc số ngày giao dịch chứng khoán
        a = list(map(int, input().split()))  # Đọc giá chứng khoán của n ngày
        
        result_str = ""  # Chuỗi để lưu kết quả nhịp chứng khoán
        
        for i in range(n):  # Duyệt qua từng ngày
            pulse_count = 1  # Khởi tạo biến đếm nhịp, ít nhất là 1 (tính cho ngày hiện tại)
            
            # Duyệt ngược về các ngày trước ngày thứ i để tính nhịp chứng khoán
            for j in range(i - 1, -1, -1):
                if a[j] <= a[i]:
                    pulse_count += 1  # Nếu giá ngày j bé hơn hoặc bằng ngày i, tăng biến đếm
                else:
                    break  # Nếu giá ngày j lớn hơn ngày i, dừng vòng lặp
            
            result_str += str(pulse_count)  # Thêm nhịp chứng khoán vào chuỗi kết quả
        
        print(result_str)  # In ra chuỗi kết quả nhịp chứng khoán

if __name__ == "__main__":
    main()