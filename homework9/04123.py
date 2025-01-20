directions = [(1, 2), (2, 1), (-1, 2), (-2, 1), (-1, -2), (-2, -1), (1, -2), (2, -1)]

def dfs(board, x, y, steps, total_steps, visited):
    if steps == total_steps:
        return 1
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and (nx, ny) not in visited:
            count += dfs(board, nx, ny, steps + 1, total_steps, visited|{(nx,ny)})
    return count

t = int(input())
for _ in range(t):
    n, m, x0, y0 = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    visited = {(x0, y0)}
    result = dfs(board, x0, y0, 1, n * m, visited)
    print(result)