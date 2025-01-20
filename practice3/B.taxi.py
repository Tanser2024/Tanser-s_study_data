n=int(input())
lst=input().split()
num1=lst.count("1")
num2=lst.count("2")
num3=lst.count("3")
num4=lst.count("4")
cars=num4+num3+(num2-1)//2+1
rest=[0,2]
if num1>num3+rest[num2%2]:
    cars+=(num1-1-num3-rest[num2%2])//4+1
print(cars)