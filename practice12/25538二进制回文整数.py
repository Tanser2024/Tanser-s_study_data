string=bin(int(input()))
for i in range(len(string)//2+1):
    if string[i+2]!=string[len(string)-1-i]:
        print("No")
        exit()
print("Yes")