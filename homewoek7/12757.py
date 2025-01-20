dic={'negative': -1,'zero': 0,'one': 1,'two': 2,'three': 3,'four': 4,'five': 5,'six': 6,'seven': 7,'eight': 8,'nine': 9,'ten': 10,'eleven': 11,'twelve': 12,'thirteen': 13,'fourteen': 14,'fifteen': 15,'sixteen': 16,'seventeen': 17,'eighteen': 18,'nineteen': 19,'twenty': 20,'thirty': 30,'forty': 40,'fifty': 50,'sixty': 60,'seventy': 70,'eighty': 80,'ninety': 90,'hundred': 100,'thousand': 1000,'million': 1000000}
inputs=list(input().split())
if "negative" in inputs:
    a=-1
    inputs=inputs[1:]
else:
    a=1
num=0
time=0
for k in ["million","thousand","hundred"]:
    time+=1
    if k in  inputs:
        n=0
        m=inputs[:inputs.index(k)]
        if "hundred" in m:
            m1 = m[:m.index("hundred")]
            for i in range(len(m1)):
                n += dic[m1[i]]
            n *=  100
            m = m[m.index("hundred") + 1:]
        for i in range(len(m)):
            n+=dic[m[i]]
        num+=n*dic[k]
        inputs=inputs[inputs.index(k)+1:]
for i in range(len(inputs)):
    num += dic[inputs[i]]
print(a*num)