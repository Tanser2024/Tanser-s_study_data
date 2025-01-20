n,k=map(int,input().split())
lst=sorted(list(map(int,input().split())))
num=0
i=0
j=0
while i + j <n-1:
    if lst[i]+lst[n-1-j]==k:
        num+=1
        i+=1
    elif lst[i]+lst[n-1-j]>k:
        j+=1
    else:
        i+=1
print(num)
