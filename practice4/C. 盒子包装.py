n=int(input())
boxes=list(map(int,input().split()))
visible=0
while True:
    b = set(boxes)
    if not b:
        break
    for i in b:
        boxes.remove(i)
    visible+=1
print(visible)
