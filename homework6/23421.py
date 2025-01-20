n,b=map(int,input().split())
values=list(map(int,input().split()))
weights=list(map(int,input().split()))
def max_value(bag,v,w):
    if len(v)==1:
        if bag>=w[0]:
            return v[0]
        else:
            return 0
    else:
        if bag>=w[-1]:
            return max(max_value(bag-w[-1],v[:-1],w[:-1])+v[-1],max_value(bag,v[:-1],w[:-1]))
        else:
            return max_value(bag,v[:-1],w[:-1])
print(max_value(b,values,weights))