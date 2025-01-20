n=int(input())
lst=sorted(list(map(int,input().split())))
K=int(input())
num=0
for i in lst:
    for j in lst[lst.index(i)+1:]:
        if i + j == K:
            num+=1
print(num)
