n=int(input())
matrix=[list(map(int,input().split())) for _ in range(n)]
if n==1:
    print(matrix[0][0])
    exit()
bottom=0;top=n-1;left=0;right=n-1;s=-float("inf")
if n%2==1:
    s=matrix[n//2][n//2]
for i in range(n//2):
    new_s=sum(matrix[bottom+i][j] for j in range(left+i,right-i+1))+sum(matrix[top-i][j] for j in range(left+i,right-i+1))+sum(matrix[j][left+i] for j in range(bottom+1+i,top-i))++sum(matrix[j][right-i] for j in range(bottom+1+i,top-i))
    s=max(s,new_s)
print(s)