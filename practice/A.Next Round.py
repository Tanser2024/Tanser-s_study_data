n,k=map(int,input().split())
scores=list(map(int,input().split()))
winners_scores=list(i for i in scores if i >=scores[k-1] and i >0)
print(len(winners_scores))