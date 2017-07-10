'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
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