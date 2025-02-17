def count_bdn(current_bdn, limit_str):
    """
    Đếm số lượng số BDN (Binary Digit Number - số chỉ chứa các chữ số 0 và 1) 
    nhỏ hơn hoặc bằng giới hạn cho trước
    
    Args:
        current_bdn (str): Số BDN hiện tại đang xét
        limit_str (str): Giới hạn dạng chuỗi
    
    Returns:
        int: Số lượng số BDN thỏa mãn
    """
    # Nếu số BDN hiện tại lớn hơn hoặc bằng giới hạn, không tính và dừng đệ quy
    if len(current_bdn) > len(limit_str) or (len(current_bdn) == len(limit_str) and current_bdn >= limit_str):
        return 0
    
    count = 0
    if current_bdn:  # Nếu chuỗi BDN không rỗng
        count = 1    # Tính là một số BDN hợp lệ
    
    next_bdn_0 = current_bdn + "0"
    next_bdn_1 = current_bdn + "1"
    
    # Đệ quy cho trường hợp thêm '0'
    count += count_bdn(next_bdn_0, limit_str)
    
    # Đệ quy cho trường hợp thêm '1'
    count += count_bdn(next_bdn_1, limit_str)
    
    return count

def main():
    t = int(input())  # Đọc số lượng bộ test
    
    for _ in range(t):  # Xử lý từng bộ test
        n = int(input())  # Đọc giới hạn N
        n_str = str(n)    # Chuyển N sang dạng chuỗi
        
        # Gọi hàm đếm số BDN bắt đầu từ số '1' và giới hạn là N
        result = count_bdn("1", n_str)
        print(result)

if __name__ == "__main__":
    main()