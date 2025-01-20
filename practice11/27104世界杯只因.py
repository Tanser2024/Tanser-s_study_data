n=int(input())
a=list(map(int,input().split()))
b=sorted([(max(i+1-a[i],0),min(i+1+a[i],n)) for i in range(n)],key=lambda x:(x[0],-x[1]))

r=0
num=0

right=0

for i in range(n):
    left = b[i][0]; right=b[i][1]
    if left<=r+1:
        num+=1

        r=right


print(num)
"""N = int(input())
a = list(map(int, input().split()))
intervals = [(max(0, i-a[i]), min(N-1, i+a[i])) for i in range(N)]
intervals.sort()

ans = 0
right = 0
temp = -1
index = 0
while index < N and right < N:
    while index < N and intervals[index][0] <= right:
        temp = max(temp, intervals[index][1])
        index += 1
    right = temp + 1
    ans += 1

print(ans)"""
"""
#夏天明2300017735;				time: 537ms
#罗景轩2300012610
n = int(input())
a = list(map(int, input().split()))
ends = [0]*n
for i in range(n):
    ends[max(i - a[i], 0)] = max(ends[max(i - a[i], 0)], i + a[i] + 1)
    
l, r = -1, 0
ans = 0
while r < n:
    l, r = r, max(ends[l + 1: r + 1])
    ans += 1
print(ans)"""