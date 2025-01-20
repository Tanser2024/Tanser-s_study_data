n=bin(int(input()))
num=n[2:]
length=len(num)
times=0
for i in range(length):
    if num[i]==num[length-1-i]:
        times+=1
    else:
        break
if times==length:
    print("Yes")
else:
    print("No")
