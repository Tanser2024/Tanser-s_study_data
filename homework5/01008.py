
d={ "pop":1,"no":2,"zip":3,"zotz":4,"tzec":5,"xul":6,"yoxkin":7,"mol":8,"chen":9,"yax":10,"zac":11,"ceh":12,"mac":13,"kankin":14,"muan":15,"pax":16,"koyab":17,"cumhu":18,"uayet":19}
l={"1":"imix","2":"ik","3":"akbal","4":"kan","5":"chicchan","6":"cimi","7":"manik","8":"lamat","9":"muluk","10":"ok","11":"chuen","12":"eb","13":"ben","14":"ix","15":"mem","16":"cib","17":"caban","18":"eznab","19":"canac","20":"ahau"}
n1=int(input())
print(n1)
for _ in range(n1):
    n=list(input().split())
    days = int(n[2]) * 365 + (d[n[1]] - 1) * 20 + int(n[0].rstrip(".")) + 1
    years = (days - 1) // 260
    da = l[str((days-1) % 20+1)]
    months = (days - 1) % 13 + 1
    print(months, da, years)



