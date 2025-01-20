import math
A=input()
def sqrt_able(x):
    if x[0]=="0":
        return False
    y=math.sqrt(int(x))
    if math.ceil(y)==int(y):
        return True
    else:
        return False
flag=False
def dfs(a):
    global flag
    if len(a)==0:
        flag=True
        return
    for i in range((len(a))):
        if sqrt_able(a[:i+1]):
            dfs(a[i+1:])
dfs(A)
print("Yes" if flag else "No")