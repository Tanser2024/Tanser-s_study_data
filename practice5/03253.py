def jsf(n0, p0, m0, child):
    if len(n0)==1:
        child.append(n0[0])
        return child
    else:
        l=(p0+m0-2)%len(n0)
        child.append(n0.pop(l))  # 使用 pop 方法移除并获取指定索引处的元素
        return jsf(n0, l + 1, m0, child)
while True:
    n,p,m=map(int,input().split())
    n1=list(range(1,n+1))
    c=[]
    if n==0:
        break
    print(",".join(map(str,jsf(n1,p,m,c))))
