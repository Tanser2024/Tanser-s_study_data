from functools import lru_cache
import sys
from sys import maxsize

sys.setrecursionlimit(10**9)
@lru_cache(maxsize=None)
def dfs(m,n,k):
    if m<k:
        return dfs(m,n,m)
    if m>n*k:
        return 0
    if m==n*k or m==0 or m==1:
        return 1
    return dfs(m-k,n-1,k)+dfs(m,n,k-1)

t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    num=dfs(m,n,m)
    print(num)