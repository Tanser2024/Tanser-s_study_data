from functools import lru_cache
@lru_cache(maxsize=None)
def dfs(n,k):
    if n==k:
        return 1
    elif k==1:
        return 1
    elif n<k or k==0:
        return 0
    else:
        temp=0
        for i in range(1,n):
            temp+=dfs(i,k-1)
        return temp
n,k=map(int,input().split())
print(dfs(n,k))