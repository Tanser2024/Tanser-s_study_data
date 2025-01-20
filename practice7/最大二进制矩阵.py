"""def max_matrix(m,ki,nl):
    j=0
    if ki>nl*nl:
        return [-1]
    if k ==0:
        return m
    if ki==1:
        m[0][0]=1
        return m
    while ki>=2*nl-1:
        for i in range(j,j+nl):
            m[j][i]=m[i][j]=1
        ki-=(2*nl-1)
        nl-=1;j+=1
    x=(ki-1)//2+1
    for i in range(j,j+x):
        m[j][i]=m[i][j]=1
    ki-=(2*x-1)
    while ki:
        m[j+1][j+1]=1
        j+=1
        ki-=1
    return m
n,k=map(int,input().split())
matrix=[[0]*n for _ in range(n)]
result = max_matrix(matrix,k,n)
if result==[-1]:
    print("-1")
else:
    for line in result:
        print(" ".join(map(str, line)))"""
n, k = map(int, input().split())
num = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        if k > 1 and i != j:
            num[i][j] = 1
            num[j][i] = 1
            k -= 2
        elif k > 0 and i == j:
            num[i][i] = 1
            k -= 1

if k == 0:
    for row in num:
        print(*row)
else:
    print("-1")