#硬币找零
a=[1,2,5]
def search(n,idx): ##递归
    if n==0:
        return 1
    if idx>=len(a) or n<0:
        return 0
    return search(n,idx+1)+search(n-a[idx],idx)
def search2(n):##动态规划
    dp=[[0 for i in range(n+1)] for j in range(len(a)+1)]
    for i in range(len(a)+1):
        dp[i][0]=1
    for i in range(1,len(a)+1):
        for j in range(1,n+1):
            dp[i][j]=0
            for k in range(j/a[i-1]+1):
                dp[i][j]+=dp[i-1][j-k*a[i-1]]
    return dp[len(a)][n]
print search2(8)