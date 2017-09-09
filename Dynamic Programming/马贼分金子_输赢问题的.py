'''
A、B两伙马贼意外地在一片沙漠中发现了一处金矿，双方都想独占金矿，但各自的实力都不足以吞下对方，经过谈判后，双方同意用一个公平的方式来处理这片金矿。处理的规则如下：他们把整个金矿分成n段，由A、B开始轮流从最左端或最右端占据一段，直到分完为止。 
马贼A想提前知道他们能分到多少金子，因此请你帮忙计算他们最后各自拥有多少金子?（两伙马贼均会采取对己方有利的策略）


								
输入
测试数据包含多组输入数据。输入数据的第一行为一个正整数T(T<=20)，表示测试数据的组数。然后是T组测试数据，每组测试数据的第一行包含一个整数n，下一行包含n个数（n <= 500 ），表示每段金矿的含金量，保证其数值大小不超过1000。

样例输入
2 
6
4 7 2 9 5 2
10
140 649 340 982 105 86 56 610 340 879

输出
对于每一组测试数据，输出一行"Case #id: sc1 sc2"，表示第id组数据时马贼A分到金子数量为sc1，马贼B分到金子数量为sc2。详见样例。

样例输出
Case #1: 18 11
Case #2: 3206 981

时间限制
C/C++语言：1000MS其它语言：3000MS	
内存限制
C/C++语言：65536KB其它语言：589824KB
'''
t=int(raw_input())
for k in range(t):
    n=int(raw_input())
    a=[int(x) for x in raw_input().split(' ')]
    a.insert(0,0)
    sum1=[0]*(n+1)
    sum1[0]=0
    for i in range(1,n+1):
        sum1[i]=sum1[i-1]+a[i]
    dp=[[0 for x in range(n+1)] for y in range(n+1)]
    for i in range(1,n+1):
        dp[i][i]=a[i]
    for i in range(1,n+1):
        for j in range(n-i+1):
            dp[j][i+j]=(sum1[i+j]-sum1[j-1])-min(dp[j+1][i+j],dp[j][i+j-1])
    print "Case #%d: " % (k+1)+str(dp[1][n])+' '+str(sum1[n]-dp[1][n])

	
	
#解法2
def PredictTheWiner3(nums):
    n=len(nums)
    dp = [[0 for i in range(n)] for j in range(n)]
    if n==1 or n==2:
        return True
    for i in range(n-1):
        dp[i][i]=nums[i]
        dp[i][i+1]=max(nums[i],nums[i+1])
    for j in range(3,n+1):
        for i in range(n-j+1):
            jj=i+j-1
            dp[i][jj]=max(nums[i]+min(dp[i+1][jj-1],dp[i+2][jj]),nums[jj]+min(dp[i+1][jj-1],dp[i][jj-2]))
    return dp[0][len(nums)-1]
print PredictTheWiner3(nums)+' '+str(sum[nums]-PredictTheWiner3(nums))

#http://blog.csdn.net/qq_28618765/article/details/65934824