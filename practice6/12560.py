def get_neighbors_count(grid, i, j, n, m):
    count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dx, dy in directions:
        nx, ny = i + dx, j + dy
        if 0 <= nx < n and 0 <= ny < m:
            count += grid[nx][ny]
    return count


def update_grid(grid, n, m):
    new_grid = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            neighbors_count = get_neighbors_count(grid, i, j, n, m)
            if grid[i][j] == 1:
                if neighbors_count < 2 or neighbors_count > 3:
                    new_grid[i][j] = 0
                else:
                    new_grid[i][j] = 1
            else:
                if neighbors_count == 3:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0

    return new_grid


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m = int(data[1])
    grid = []
    index = 2
    for i in range(n):
        row = [int(x) for x in data[index:index + m]]
        grid.append(row)
        index += m

    new_grid = update_grid(grid, n, m)

    for i in range(n):
        print(' '.join(map(str, new_grid[i])))


if __name__ == "__main__":
    main()