import math

num=0
while True:
    num+=1
    n,d=map(int,input().split())
    D=d*d
    if n==0:
        break
    islands=[]
    for _ in range(n):
        x,y=map(int,input().split())
        islands.append([x,y])
    if any(island[1]>d for island in islands):
        print(f"Case {num}: -1")
    else:
        s=[]
        for i in range(n):
            l = islands[i][0] - math.sqrt(D - islands[i][1] ** 2)
            r = islands[i][0] + math.sqrt(D - islands[i][1] ** 2)
            s.append([l,r])
        s.sort()
        count = 0
        end = float('-inf')
        for left, right in s:
            if left > end:
                count += 1
                end = right
            else:
                # 更新右侧边界
                end = min(end, right)
        print(f"Case {num}: {count}")
    input().strip()