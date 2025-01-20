n=int(input())
st=list(map(int,input().split()))
stu=[(st[i],i+1) for i in range(n)]
s=sorted(stu)
sets=[str(stu.index(i)+1) for i in s]
stu_time=[(n-i-1)*s[i][0] for i in range(n)]
print(" ".join(sets))
print("%.2f"%(sum(stu_time)/n))