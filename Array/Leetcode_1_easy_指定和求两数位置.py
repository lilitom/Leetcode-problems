'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8
#高级方法
#采用异或的方法
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if target-nums[i] in nums:
                if not nums.index(target-nums[i])==i:
                    return [i,nums.index(target-nums[i])]
slu=Solution()
t=slu.missingNumber([1,2,3,4,6]，7)
printt






#参考：
#https://leetcode.com/problems/two-sum/#/description