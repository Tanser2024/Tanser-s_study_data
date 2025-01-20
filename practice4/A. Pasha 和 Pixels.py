n, m, k = map(int, input().split())
mat = [[0 for _ in range(m)] for _ in range(n)]
num = 0

for i in range(1, k + 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    mat[a][b] = 1

    # 检查是否形成了特定的形状
    if (a < n - 1 and b > 0 and
            mat[a + 1][b - 1] == 1 and mat[a + 1][b] == 1 and mat[a][b - 1] == 1):
        print(i)
        break
    elif (a < n - 1 and b < m - 1 and
          mat[a + 1][b] == 1 and mat[a + 1][b + 1] == 1 and mat[a][b + 1] == 1):
        print(i)
        break
    elif (a > 0 and b < m - 1 and
          mat[a - 1][b] == 1 and mat[a - 1][b + 1] == 1 and mat[a][b + 1] == 1):
        print(i)
        break
    elif (a > 0 and b > 0 and
          mat[a - 1][b - 1] == 1 and mat[a - 1][b] == 1 and mat[a][b - 1] == 1):
        print(i)
        break
    else:
        num += 1

if num == k:
    print(0)
