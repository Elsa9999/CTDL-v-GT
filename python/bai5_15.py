def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        ans = [0] * n  # Initialize the answer list

        for i in range(n):
            nge = -1
            nge_index = -1

            # Find Next Greater Element (NGE)
            for j in range(i + 1, n):
                if a[j] > a[i]:
                    nge = a[j]
                    nge_index = j
                    break

            if nge != -1:
                nse_of_nge = -1
                # Find Next Smaller Element (NSE) of NGE
                for k in range(nge_index + 1, n):
                    if a[k] < nge:
                        nse_of_nge = a[k]
                        break
                ans[i] = nse_of_nge
            else:
                ans[i] = -1

        print(*ans)  # Print the list elements separated by spaces

solve()