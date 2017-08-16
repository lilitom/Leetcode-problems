'''
Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
nums=[1,1,1,2,2,2,3,3,3,4,4,4,5,6,6,6,7,7,7,8,8,8,9,9,9] 
Êä³ö5
'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        res=0
        for i in range(32):
            sum=0
            for j in range(len(nums)):
                sum+=(nums[j]>>i)&1
            res|=(sum%3)<<i
			#res+=(sum%3)<<i
        if res >= 2**31:
            res -= 2**32
        return res
#²Î¿¼
#https://leetcode.com/problems/single-number-ii/description/
#http://www.cnblogs.com/springfor/p/3870863.html

