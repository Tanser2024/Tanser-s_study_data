from collections import deque

def bfs(matrix):
    m, n = len(matrix), len(matrix[0])
    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    queue = deque([(0, 0, 0)])
    visited = {(0, 0)}

    while queue:
        x, y, step = queue.popleft()
        if matrix[x][y] == 1:
            return step
        for dx, dy in directions:
            tx, ty = x + dx, y + dy
            if 0 <= tx < m and 0 <= ty < n and (tx, ty) not in visited and matrix[tx][ty] != 2:
                visited.add((tx, ty))
                queue.append((tx, ty, step + 1))
    return "NO"


N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

result = bfs(matrix)
print(result)