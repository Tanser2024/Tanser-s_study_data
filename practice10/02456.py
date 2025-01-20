N,C=map(int,input().split())
set_of_fetch=sorted([int(input()) for _ in range(N)])

def is_valid(gap):
    cur=set_of_fetch[0]
    count=1
    for i in range(1,N):
        if set_of_fetch[i]-cur>=gap:
            cur=set_of_fetch[i]
            count+=1
    return count>=C

def max_gap(fetch):
    right=(fetch[-1]-fetch[0])//C
    left=0
    while left<=right:
        gap=(left+right)//2
        if is_valid(gap):
            left=gap+1
        else:
            right=gap-1
    return left

print(max_gap(set_of_fetch))

