
from collections import deque

nums,k=map(int,input().split())

data=list(map(int,input().split()))
q=deque(data[:k])
max_num=max(q)
results=[max_num]
for num in data[k:]:
    taken_num=q.popleft()
    if taken_num<max_num:
        max_num=max(max_num,num)
        q.append(num)
    else:
        q.append(num)
        max_num=max(q)
    results.append(max_num)

print(*results)
