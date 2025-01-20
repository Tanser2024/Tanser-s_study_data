import sys

from collections import deque

data=sys.stdin.read().split()
data=deque(data)
pig=[];min_weight=float("inf")
while data:
    d=data.popleft()
    if d=="pop":
        if pig:
            p=pig.pop()
            if p==min_weight and pig:
                min_weight=min(pig)
    elif d=="push":
        weight=data.popleft()
        pig.append(int(weight))
        min_weight=min(min_weight,int(weight))
    else:
        if pig:
            print(min_weight)