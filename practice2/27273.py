def sum_data(a):
    a=int(a)
    b=a*(a+1)//2
    c=0
    d=1
    while d<=a:
        c=c+d
        d*=2
    print(b-2*c)
t=int(input())
for _ in range(t):
    i = input()
    sum_data(i)
