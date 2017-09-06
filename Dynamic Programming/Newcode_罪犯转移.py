#问题解释
'''
C市现在要转移一批罪犯到D市，C市有n名罪犯，按照入狱时间有顺序，另外每个罪犯有一个罪行值，值越大罪越重。现在为了方便管理，市长决定转移入狱时间连续的c名犯人，同时要求转移犯人的罪行值之和不超过t，问有多少种选择的方式？ 
输入描述:
第一行数据三个整数:n，t，c(1≤n≤2e5,0≤t≤1e9,1≤c≤n)，第二行按入狱时间给出每个犯人的罪行值ai(0≤ai≤1e9)
输出描述:
一行输出答案。
示例1
输入

3 100 2
1 2 3
输出

2
'''
# coding=utf-8
n,t,c=map(int,raw_input().strip().split())
nums=[int(x) for x in raw_input().split()]
ways=0
if len(nums)>c:
    s=sum(nums[:c])
    if s<=t:
        ways=ways+1
    for i in range(c,len(nums)):
        s+=nums[i]-nums[i-c]  #这里的计算比较巧妙
        if s<=t:
            ways+=1
print ways


#https://www.nowcoder.com/practice/b7b1ad820f0a493aa128ed6c9e0af448?tpId=49&&tqId=29287&rp=1&ru=/activity/oj&qru=/ta/2016test/question-ranking