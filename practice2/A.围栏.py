def judge(a):
    a=int(a)
    if 360%(180-a)==0:
        print("YES")
    else:
        print("NO")
t=int(input())
for _ in range(t):
    q=input()
    judge(q)