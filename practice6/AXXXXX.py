def rest(i,x):
    return int(i)%x
def longest_array(a,x):
    s=[rest(i,x) for i in a]
    if sum(a)%x!=0:
        return len(a)
    else:
        for i in range(len(a)//2+1):
            if s[i]!=0 or s[len(a)-1-i]!=0:
                return len(a)-1-i
        return -1
t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    A=list(map(int,input().split()))
    print(longest_array(A,x))