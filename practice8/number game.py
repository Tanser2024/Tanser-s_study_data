"""for _ in range(int(input())):
	n = int(input())
	a = sorted(list(map(int, input().split())))
	for k in range(n, -1, -1):
		if all(k - 1 + i < n and a[k - 1 + i] <= i + 1 for i in range(k)):
			print(k)
			break"""
t = int(input())
for _ in range(t):
    n = int(input())
    lis = [int(x) for x in input().split()]
    lis.sort()
    num = lis.count(1)
    s = min(num,n//2+n%2)
    check = False
    for k in range(1,s+1):
        lists = lis[k-1:2*k-1]
        for i in range(k):
            if lists[i] > i+1:
                check = True
                break
        if check:
            s = k-1
            break
    print(s)