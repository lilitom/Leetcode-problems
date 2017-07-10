'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
I：一条直线上有n座房子，每座房子里都有一定的现金（用nums[i]表示），不能
同时抢劫相邻的两座房子，问最多能抢劫多少钱？这是一道典型的动态规划，用
money[i]表示从第1座房子到第i座房子能抢到的最多的钱，
那么money[i] = max(money[i - 2] + nums[i], money[i - 1])。
'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------
#标准方法--牛 the best way-niu


'''
f(0) = nums[0]
f(1) = max(num[0], num[1])
f(k) = max( f(k-2) + nums[k], f(k-1) )
'''
class Solution:
    
    def rob(self, nums):
        
        last, now = 0, 0
        
        for i in nums: last, now = now, max(last + i, now)
                
        return now
		
		
		
		


#------------------------------------------------------------------------------------
#我的方法 my way
#coding=utf-8
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)==0:return 0
        dp=[0]*(len(nums)+1)
        dp[1]=nums[0]
        for i in range(2,len(nums)+1):
            dp[i]=max(dp[i-2]+nums[i-1],dp[i-1])
        return max(dp)

cc=Solution()
t=cc.rob([1,1,1])
print t



#来自：https://leetcode.com/problems/house-robber/#/solutions