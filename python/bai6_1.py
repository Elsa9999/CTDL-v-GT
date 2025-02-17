def decimal_to_binary(n):
    """
    Chuyển đổi một số thập phân dương sang dạng nhị phân
    
    Args:
        n (int): Số thập phân dương cần chuyển đổi
    
    Returns:
        str: Chuỗi nhị phân tương ứng với số n
    """
    if n == 0:
        return "0"  # Trường hợp đặc biệt: nếu số đầu vào là 0, trả về chuỗi "0"
    
    binary_string = ""
    
    # Vòng lặp while để thực hiện chuyển đổi từ thập phân sang nhị phân
    while n > 0:
        remainder = n % 2  # Tính phần dư khi n chia cho 2
        binary_string = str(remainder) + binary_string  # Thêm phần dư vào đầu chuỗi
        n //= 2  # Chia nguyên n cho 2
    
    return binary_string

def main():
    t = int(input())  # Đọc số lượng test case
    
    for _ in range(t):  # Vòng lặp để xử lý t test case
        n = int(input())  # Đọc số tự nhiên n
        
        # Chuyển đổi và in các số nhị phân từ 1 đến n
        binary_numbers = [decimal_to_binary(i) for i in range(1, n + 1)]
        print(" ".join(binary_numbers))  # In các số nhị phân cách nhau bởi dấu cách

if __name__ == "__main__":
    main()