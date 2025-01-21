import time

def printPairs(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"({i}, {j})", end=" ")
    print()

n = 3  # Số lượng phần tử

start = time.time()  # Bắt đầu đo thời gian

printPairs(n)  # Chạy thuật toán

end = time.time()  # Kết thúc đo thời gian
elapsed_ms = (end - start) * 1000  # Tính thời gian bằng milliseconds

print(f"Thời gian (ms): {elapsed_ms:.2f}")
