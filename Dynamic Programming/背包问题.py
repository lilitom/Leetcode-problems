#ÏêÏ¸²Î¿¼ http://blog.csdn.net/littlethunder/article/details/26575417
# coding=utf-8
weight=[2,2,6,5,4]
value=[6,3,5,4,6]
M=10
N=len(weight)
f=[[0 for i in range(11)] for j in range(6)]
for i in range(1,N+1):
    for j in range(1,M+1):
        if weight[i-1]<=j:
            f[i][j]=max(f[i-1][j],f[i-1][j-weight[i-1]]+value[i-1])
        else:
            f[i][j]=f[i-1][j]
print f[N][M]