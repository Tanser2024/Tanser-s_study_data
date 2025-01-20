n,d=map(int,input().split())
line=[int(input()) for i in range(n)]
check=[False]*n
line_new=[]
while len(line_new)<n:
    buffer=[]
    i=0
    while i<n:
        if check[i]:
            i+=1
            continue
        if len(buffer)==0:
            buffer.append(line[i])
            maxh=line[i]
            minh=line[i]
            check[i]=True
            continue
        maxh=max(maxh,line[i])
        minh=min(minh,line[i])
        if maxh<=line[i]+d and minh>=line[i]-d:
            buffer.append(line[i])
            check[i]=True
        i+=1
    buffer.sort()
    line_new.extend(buffer)
for i in line_new:
    print(i)
""""""
"""n, d = map(int, input().split())
line = [int(input()) for _ in range(n)]
check = [False] * n
line_new = []
"""
"""while len(line_new) < n:
    start = next(i for i in range(n) if not check[i])
    maxh, minh = line[start], line[start]
    buffer = [line[start]]
    check[start] = True
    for i in range(n):
        if check[i]:
            continue
        new_maxh, new_minh = max(maxh, line[i]), min(minh, line[i])
        if new_maxh <= line[i] + d and new_minh >= line[i] - d:
            buffer.append(line[i])
            maxh, minh = new_maxh, new_minh
            check[i] = True
    buffer.sort()
    line_new.extend(buffer)
for num in line_new:
    print(num)

n, d = map(int, input().split())
line: list[int] = [int(input()) for _ in range(n)]
check: list[bool] = [False] * n
line_new: list[int] = []

while len(line_new) < n:
    start = next(i for i in range(n) if not check[i])
    maxh, minh = line[start], line[start]
    buffer: list[int] = [line[start]]
    check[start] = True

    for i in range(n):
        if check[i]:
            continue
        new_maxh, new_minh = max(maxh, line[i]), min(minh, line[i])
        if new_maxh <= line[i] + d and new_minh >= line[i] - d:
            buffer.append(line[i])
            maxh, minh = new_maxh, new_minh
            check[i] = True
    buffer.sort()
    line_new.extend(buffer)
for num in line_new:
    print(num)"""