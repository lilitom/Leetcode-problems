#ÏêÏ¸²Î¿¼ http://blog.csdn.net/shizheng163/article/details/50986993
# coding=utf-8
juzhen=[[1,2,3,4],[4,8,3,2],[6,1,4,5],[7,3,7,8]]
m=len(juzhen)
n=len(juzhen[1])
dp=[[0 for i in range(n)] for j in range(m)]
for i in range(n):
    dp[0][i]=dp[0][i]+juzhen[0][i]
for i in range(m):
    dp[i][0]=dp[i][0]+juzhen[i][0]
for i in range(1,m):
    for j in range(1,n):
        dp[i][j]=max(dp[i-1][j],dp[i][j-1])+juzhen[i][j]
print dp[m-1][n-1]