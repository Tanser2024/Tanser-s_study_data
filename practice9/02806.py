import sys
lines=[line.strip().split() for line in sys.stdin.readlines()]
for word1,word2 in lines:
    m=len(word1);n=len(word2)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if word2[j-1]==word1[i-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    print(dp[-1][-1])