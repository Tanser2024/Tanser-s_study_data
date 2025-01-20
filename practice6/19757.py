def min_p(r,lst,num):
    if num==1:
        return 1
    lst.sort()
    right=lst[0]+r
    a=lst[0]
    nums=1
    for i in range(1,num):
        if lst[i]<=right:
            if lst[i]-r<=a:
                right=lst[i]+r
        else:
            right=lst[i]+r
            a=lst[i]
            nums+=1
    return nums
while True:
    R,n=map(int,input().split())
    l=list(map(int,input().split()))
    if R==-1 and n==-1:
        break
    print(min_p(R,l,n))