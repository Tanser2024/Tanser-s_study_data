def min_time(l,n):
    times=[min(l-i,i) for i in n]
    return max(times)
def max_time(l,n):
    times=[max(l-i,i) for i in n]
    return max(times)
t=int(input())
for _ in range(t):
    le,num=map(int,input().split())
    ne=list(map(int,input().split()))
    print(min_time(le,ne),max_time(le,ne))
