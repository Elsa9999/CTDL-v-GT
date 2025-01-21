import time

def print_numbers(n):
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

n = 5
start = time.time()  # Bắt đầu đo thời gian

print_numbers(n)  # Chạy thuật toán

end = time.time()  # Kết thúc đo thời gian
elapsed_ms = (end - start) * 1000

print(f"Thời gian (ms): {elapsed_ms:.2f}")
