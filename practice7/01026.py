import copy


while True:
    n=int(input())
    if n==0:
        break
    Code=list(map(int,input().split()))
    c = [Code.index(x)+1 for x in range(1, n + 1)]
    position_map = {i: c[i] - 1 for i in range(n)}
    d=list(range(n))
    num=[]
    for i in range(1000000):
        d=[d[position_map[i]] for i in range(n)]
        if d==list(range(n)):
            num.append(i+1)
            break
    while True:
        inputs=list(input().split())
        k=int(inputs[0])
        if k==0:
            break
        data0 = list(" ".join(inputs[1:]))
        data = data0 + [" "] * (n - len(data0))
        k=k%num[0]

        for _ in range(k):
            data = [data[position_map[i]] for i in range(n)]
        print("".join(data))
