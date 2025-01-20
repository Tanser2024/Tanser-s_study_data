def min_time(a,b):
    zipped = sorted(list(zip(a, b)), key=lambda x: (x[0], x[1]), reverse=True)
    time = 0
    for ai,bi in zipped:
        if time + bi >= ai:
            time = max(ai, time)
            break
        else:
            time += bi
    return time
t=int(input())
for _ in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    B = list(map(int, input().split()))

    print(min_time(A,B))