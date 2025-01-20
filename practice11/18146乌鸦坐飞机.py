n,k=map(int,input().split())
nums=list(map(int,input().split()))

num1=num2=num3=0
num_of_num3=0
for n in nums:
    num=n%4
    if num==1:
        num1+=1
    elif num==2:
        num2+=1
    else:
        num3+=1
        num_of_num3+=n//4
s=sum(num//4 for num in nums)
if sum(nums)<=8*n:
    if s<=n :
        rest_4=n-s;rest_2=2*n
        if num3>=rest_4:
            rest_2+=2*(rest_4-num3)
            print("YES" if num2+num1 <=rest_2 else "NO")
        else:
            temp=rest_4-num3
            if num1<=temp:
                rest_2+=temp
            else:
                rest_2+=(temp-(num1-temp))
            print("YES" if num2 <= rest_2 else "NO")

    else:
        rest_2=2*n-(s-n)*2
        print("YES" if num2 + num1 +2*num3 <= rest_2 else "NO")

else:
    print("NO")

