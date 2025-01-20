"""a=input()
b=eval(a[:a.index("=")])
c=float(a[a.index("=")+1:])
if round(b,2)==c:
    print("true")
else:
    print("false")"""
a=input()
n=int(input())
information=input()
d=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
D=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
num=["0","1","2","3","4","5","6","7","8","9"]
string=[]
if a in ["e","E","encrypt","Encrypt"]:
    for i in information:
        if i in d:
            string.append(d[(d.index(i)+n)%26])
        elif i in D:
            string.append(D[(D.index(i) + n) % 26])
        elif i in num:
            string.append(num[(num.index(i)+n)%10])
        else:
            string.append(i)
    print("".join(string))
elif a in ["d","D","decrypt","Decrypt"]:
    for i in information:
        if i in d:
            string.append(d[(d.index(i)-n)%26])
        elif i in D:
            string.append(D[(D.index(i) - n) % 26])
        elif i in num:
            string.append(num[(num.index(i)-n)%10])
        else:
            string.append(i)
    print("".join(string))
else:
    print("Wrong Mode")



