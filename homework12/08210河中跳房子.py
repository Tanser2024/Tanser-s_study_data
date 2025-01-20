l,n,m=map(int,(input().split()))
stones=[0]+[int(input()) for _ in range(n)]+[l]
gap=[stones[i+1]-stones[i] for i in range(n+1)]

def is_valid(distance):
    ans=0
    num=0
    for i in range(n+1):
        ans+=gap[i]
        if ans>=distance:
            ans=0
        else:
            num+=1

            if num>m:
                return False
    return True

left=0;right=l//(n-m+1)
while left<right:
    mid=(left+right+1)//2
    if is_valid(mid):
        left=mid
    else:
        right=mid-1
print(left)

