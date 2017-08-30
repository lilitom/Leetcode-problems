'''
Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return False.
Example 2:
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
Note:
1 <= length of the array <= 20.
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.
'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8



#------------------------------------------------------------------------------------
def PredictTheWiner(nums):
    n=len(nums)
    if n==1 or n==2:
        return True
    dp=[0]*n
    for i in range(n-1,-1,-1):
        for j in range(i,n):
            if i==j:
                dp[i]=nums[i]
            else:
                dp[j]=max(nums[i]-dp[j],nums[j]-dp[j-1])
    return dp[n-1]>=0
def PredictTheWiner2(nums):
    n=len(nums)
    if n==1 or n==2:
        return True
    dp=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        dp[i][i]=nums[i]
    for i in range(1,n):
        for j in range(n-i):
            jj=j+i
            dp[i][jj]=max(nums[jj]-dp[i][jj-1],nums[i]-dp[i+1][jj])
    return dp[0][n-1]>=0
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
    if dp[0][n-1]>=(sum(nums)+1)/2:
        return True
    else:
        return False
Result=PredictTheWiner3([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
print Result





#Recursive
nums=[1,5,233,7]
def PredictWiner(nums):
    if nums==None or len(nums)<1:
        return False
    totalsum=sum(nums)
    firstPlaySum=helper(nums,0,len(nums)-1)
    secondPlaySum=totalsum-firstPlaySum
    return firstPlaySum>=secondPlaySum
def helper(nums,start,end):
    if start>end:
        return 0
    first=nums[start]+min(helper(nums,start+2,end),helper(nums,start+1,end-1))
    last=nums[end]+min(helper(nums,start+1,end-1),helper(nums,start,end-2))
    return max(first,last)
print PredictWiner(nums)


#参考：https://leetcode.com/problems/predict-the-winner/#/description

#相似题目
# https://leetcode.com/problems/can-i-win/#/description