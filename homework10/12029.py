import sys
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def dfs(row, col):
    stack = [(row, col)]
    while stack:
        r, c = stack.pop()
        if not visited[r][c]:
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 1 <= nr <= m and 1 <= nc <= n and not visited[nr][nc] and matrix[r][c] > matrix[nr][nc]:
                    matrix[nr][nc] = matrix[r][c]
                    stack.append((nr, nc))
input = sys.stdin.read
data = input().split()
K = int(data.pop(0))
for _ in range(K):
    global m, n
    m = int(data.pop(0))
    n = int(data.pop(0))
    matrix = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            matrix[i][j] = int(data.pop(0))
    rp = int(data.pop(0))
    cp = int(data.pop(0))
    p = int(data.pop(0))
    flag=False
    for _ in range(p):
        t1 = int(data.pop(0))
        t2 = int(data.pop(0))
        visited = [[False] * (n + 1) for _ in range(m + 1)]
        dfs(t1, t2)
        if visited[rp][cp]:
            flag=True
    if flag:
        print("Yes")
    else:
        print("No")


