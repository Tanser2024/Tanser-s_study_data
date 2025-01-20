f=[1,1]
for i in range(19):
    f.append(f[i]+f[i+1])
n=int(input())
for _ in range(n):
    print(f[int(input())-1])
