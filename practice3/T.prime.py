
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
print(is_prime(151))
"""q=int(input())
lst=map(int,input().split())
for i in lst:
    num=0
    if i%2==0 and i!=4:
        print("NO")
    else:
        a=math.sqrt(i)
        if a==int(a) and i!=1:
            if is_prime(int(a)):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
"""



