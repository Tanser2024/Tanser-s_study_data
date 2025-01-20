
num=int(input())
outputs=[]
def max_s(n,k):
    if n<=4:
        if n not in outputs:
            outputs.append(n)
            return [n,outputs]
        else:
            return [0,[]]

    if k*(k+1)//2 <= n:
        return [0,[]]
    else:
        result=-float("inf")
        cur=[]
        for i in range(n):
            if i*max_s(n-i,i)[0]>result:
                result=i*max_s(n-i,i)[0]
                cur=max_s(n-i,i)[1]+[i]

        return [result,outputs+cur]
print(max_s(num,num))