from collections import deque

def bfs(grid, A, B, C, start, end):
    visited = [[[False for _ in range(C)] for _ in range(B)] for _ in range(A)]
    q = deque()

    q.append(start)
    visited[start[0]][start[1]][start[2]] = True

    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    while q:
        current = q.popleft()

        if current[0] == end[0] and current[1] == end[1] and current[2] == end[2]:
            return current[3]

        for i in range(6):
            nx = current[0] + dx[i]
            ny = current[1] + dy[i]
            nz = current[2] + dz[i]

            if 0 <= nx < A and 0 <= ny < B and 0 <= nz < C and \
               not visited[nx][ny][nz] and grid[nx][ny][nz] != '#':
                visited[nx][ny][nz] = True
                q.append((nx, ny, nz, current[3] + 1))

    return -1

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        A, B, C = map(int, input().split())

        grid = []
        start = None
        end = None

        for i in range(A):
            layer = []
            for j in range(B):
                row = list(input())  # Read the row as a list of characters
                layer.append(row)
                for k in range(C):
                    if row[k] == 'S':
                        start = (i, j, k, 0)
                    if row[k] == 'E':
                        end = (i, j, k, 0)
            grid.append(layer)

        print(bfs(grid, A, B, C, start, end))