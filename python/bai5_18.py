def main():
    t = int(input())  # Đọc số lượng bộ test
    
    for _ in range(t):  # Xử lý t bộ test
        n = int(input())  # Đọc số lượng phần tử của mảng
        a = list(map(int, input().split()))  # Đọc mảng đầu vào
        
        # Tạo frequency_map để lưu tần số xuất hiện của mỗi phần tử
        frequency_map = {}
        for num in a:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        
        ans = [0] * n  # Khởi tạo mảng kết quả
        
        # Tìm phần tử gần nhất bên phải có tần số lớn hơn
        for i in range(n):
            result = -1  # Giá trị mặc định nếu không tìm thấy
            current_frequency = frequency_map[a[i]]
            
            # Tìm phần tử gần nhất bên phải có tần số lớn hơn
            for j in range(i + 1, n):
                if frequency_map[a[j]] > current_frequency:
                    result = a[j]  # Tìm thấy phần tử thỏa mãn
                    break  # Dừng vòng lặp vì đã tìm thấy phần tử gần nhất
            
            ans[i] = result
        
        # In kết quả
        print(*ans)  # Sử dụng * để giải nén mảng khi in

if __name__ == "__main__":
    main()