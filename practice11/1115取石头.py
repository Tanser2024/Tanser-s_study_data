from functools import lru_cache
import math
import sys
sys.setrecursionlimit(1<<30)
@lru_cache()
def win_or_lose(a,b,s):
    n=math.gcd(a,b)
    a//=n;b//=n
    if a<b:
        a,b=b,a
    if a%b==0:
        return s
    if a//2<b:
        return win_or_lose(b,a-b,s+1)
    for k in range(a//b,0,-1):
        if win_or_lose(a-k*b,b,s+1)%2==0:
            return s
    return s+1
while True:
    a,b=map(int,input().split())

    if a==0:
        break
    if win_or_lose(a,b,0)%2==0:
        print("win")
    else:
        print("lose")