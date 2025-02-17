def largest_rectangle_area(heights):
    """
    Tính diện tích hình chữ nhật lớn nhất trong histogram
    
    Args:
        heights (list[int]): Danh sách chiều cao của các cột histogram
    
    Returns:
        int: Diện tích hình chữ nhật lớn nhất tìm được
    """
    n = len(heights)  # Lấy số lượng cột trong histogram
    stack = []  # Khởi tạo stack để lưu trữ index của các cột
    max_area = 0  # Khởi tạo biến lưu diện tích hình chữ nhật lớn nhất, ban đầu là 0
    
    # Duyệt qua từng cột của histogram, từ cột đầu tiên đến cột cuối cùng
    # Thêm một cột ảo vào cuối histogram (với i <= n), cột ảo này có chiều cao là 0,
    # mục đích để đảm bảo tất cả các cột còn lại trong stack đều được xử lý sau vòng lặp chính
    for i in range(n + 1):
        # Xác định chiều cao hiện tại của cột đang xét
        h = 0 if i == n else heights[i]
        
        # Vòng lặp while xử lý việc tính toán diện tích khi gặp một cột có chiều cao nhỏ hơn
        # cột trên đỉnh stack, hoặc khi duyệt đến cột ảo cuối cùng
        while stack and h < heights[stack[-1]]:
            # Lấy chiều cao của cột trên đỉnh stack
            height = heights[stack.pop()]
            
            # Tính chiều rộng của hình chữ nhật
            if not stack:
                width = i  # Nếu stack rỗng, chiều rộng từ đầu histogram đến cột hiện tại
            else:
                width = i - stack[-1] - 1  # Khoảng cách giữa cột hiện tại và cột trên đỉnh stack mới
            
            # Tính diện tích hình chữ nhật hiện tại và cập nhật max_area nếu cần
            max_area = max(max_area, height * width)
        
        # Đẩy index cột hiện tại vào stack
        stack.append(i)
    
    return max_area

def main():
    t = int(input())  # Đọc số lượng test case
    
    for _ in range(t):  # Xử lý từng test case
        n = int(input())  # Đọc số lượng cột trong histogram
        heights = list(map(int, input().split()))  # Đọc chiều cao các cột
        
        # Tính và in diện tích hình chữ nhật lớn nhất
        print(largest_rectangle_area(heights))

if __name__ == "__main__":
    main()