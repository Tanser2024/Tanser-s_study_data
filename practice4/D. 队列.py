n=int(input())
time=sorted(list(map(int,input().split())))
num=0
t=0
for i in time:
    if i>=t:
        num+=1
        t+=i
print(num)